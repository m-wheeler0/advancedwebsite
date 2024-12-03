from app import db
from flask_login import UserMixin


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), index=True, unique=True)
    password = db.Column(db.String(50))
    description = db.Column(db.String(200))

    favourites = db.relationship('Game', secondary='user_favourites', backref='favourited_by')
    orders = db.relationship('Game', secondary='user_orders', backref='ordered_by')


class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    game_title = db.Column(db.String(50), index=True)
    description = db.Column(db.String(200))
    cover_image = db.Column(db.String(255), nullable=True)
    price = db.Column(db.Float)

    @property
    def favourites_count(self):
        return len(self.favourited_by)


class UserFavourites(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    game_id = db.Column(db.Integer, db.ForeignKey('game.id'), primary_key=True)


class UserOrders(db.Model):
    order_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), index=True)
    game_id = db.Column(db.Integer, db.ForeignKey('game.id'), index=True)
