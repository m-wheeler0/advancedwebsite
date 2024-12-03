import flask

from app import app, db
from flask import Flask, render_template, request, flash
from flask_login import LoginManager, login_user, logout_user, current_user
from .login_form import LoginForm, RegisterForm
from .models import User, Game, UserOrders, UserFavourites
from werkzeug.security import generate_password_hash, check_password_hash
from .recommendation_function import recommend
import json

loginManager = LoginManager()
loginManager.init_app(app)

def get_games():
    games = Game.query.all()
    return games

@app.route('/')
def index():

    if current_user.is_authenticated:
        user_orders = UserOrders.query.filter_by(user_id=current_user.id).all()
        user_favourites = UserFavourites.query.filter_by(user_id=current_user.id).all()
        user_recommendations = recommend(current_user)

        ordered_games = []
        favourited_games = []

        for object in user_orders:
            ordered_games.append(Game.query.get(object.game_id))

        ordered_games.reverse()

        for object in user_favourites:
            favourited_games.append(Game.query.get(object.game_id))

        return render_template('home.html', user_orders=ordered_games,
                               user_favourites=favourited_games,
                               recommendations=user_recommendations)
    else:
        return render_template('home.html')

@loginManager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():

        user = User.query.filter_by(username=form.username.data).first()

        if user and check_password_hash(user.password, form.password.data):
            login_user(user, remember=True)
            next = flask.request.args.get('next')
            return flask.redirect(next or flask.url_for('index'))
        else:
            flash("Invalid login credentials")
            return flask.redirect(flask.url_for('login'))
    return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        user = User(
            username=form.username.data,
            password=generate_password_hash(form.password.data)
        )
        db.session.add(user)
        db.session.commit()

        login_user(user, remember=True)
        next = flask.request.args.get('next')
        return flask.redirect(next or flask.url_for('index'))

        return flask.redirect(flask.url_for('index'))

    return render_template('register.html', form=form)

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user()
    return flask.redirect(flask.url_for('index'))

@app.route('/profile', methods=['GET', 'POST'])
def profile():
    return render_template('profile.html')

@app.route('/update_description', methods=['POST'])
def update_description():
    data = json.loads(request.data)
    new_desc = data.get('new_desc')
    user_id = int(current_user.get_id())

    user = db.session.query(User).filter_by(id=user_id).first()
    user.description = new_desc
    db.session.commit()

    return json.dumps({'status': 'OK', 'new_desc': new_desc})

@app.route('/order_game', methods=['POST'])
def order_game():
    data = json.loads(request.data)
    game_id = data.get('ordered_game_id')
    user_id = int(current_user.get_id())

    order = UserOrders(game_id=game_id, user_id=user_id)
    db.session.add(order)
    db.session.commit()

    return json.dumps({'status': 'OK', 'ordered_game_id': game_id})

@app.route('/favourite_game', methods=['POST'])
def favourite_game():
    data = json.loads(request.data)
    game_id = data.get('favourite_game_id')
    user_id = int(current_user.get_id())

    favourite = UserFavourites(game_id=game_id, user_id=user_id)
    db.session.add(favourite)

    db.session.commit()

    return json.dumps({'status': 'OK', 'favourite_game_id': game_id})

@app.route('/unfavourite_game', methods=['POST'])
def unfavourite_game():
    data = json.loads(request.data)
    game_id = data.get('unfavourite_game_id')
    user_id = int(current_user.get_id())

    favourite = UserFavourites.query.filter_by(game_id=game_id, user_id=user_id).first()
    db.session.delete(favourite)

    db.session.commit()

    return json.dumps({'status': 'OK', 'unfavourite_game_id': game_id})



@app.route('/store', methods=['GET', 'POST'])
def store():
    return render_template('store.html', games=get_games())

@app.route('/game/<int:id>')
def game_page(id):
    game = Game.query.get(id)

    return render_template('game_page.html', game=game)