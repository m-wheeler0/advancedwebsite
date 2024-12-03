def recommend(user):
    list_favourites = user.favourites
    list_similar_users = []
    recommended_games = []
    for game in list_favourites:
        favourited_by_users = game.favourited_by

        for favourited_user in favourited_by_users:
            if favourited_user != user and favourited_user not in list_similar_users:
                list_similar_users.append(favourited_user)
            else:
                continue

    for other_user in list_similar_users:
        for favourite_game in other_user.favourites:
            if favourite_game not in user.favourites and favourite_game not in recommended_games:
                recommended_games.append(favourite_game)
            else:
                continue

    return recommended_games