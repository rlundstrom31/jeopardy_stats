import json
import os
import pandas as pd

import stats
from stats.game import Game

if __name__ == '__main__':
    saved_games = os.listdir("../games/")
    games = set()
    for date in saved_games:
        with open("../games/" + str(date), "r") as read_file:
            game_data = json.load(read_file)
            game = stats.game.Game()
            for key in game_data.keys():
                game.__setattr__(key, game_data[key])
            games.add(game)
    df = pd.DataFrame([vars(game) for game in games])
    df = df.drop(columns=['URL', 'possible_score'])
    print(df['adjusted_coryat'].mean())
    print(df.tail(100)['adjusted_coryat'].mean())