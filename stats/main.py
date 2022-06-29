import json
import os
import pandas as pd
import matplotlib.pyplot as plt
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
    df['date'] = pd.to_datetime(df['date'])
    df = df.sort_values('date')

    df['rolling_adjusted_coryat'] = df.adjusted_coryat.rolling(30).mean()
    df['rolling_final'] = df.final.rolling(25).mean()
    df = df.reset_index()
    df = df.drop(columns=['index'])
    print(df)
    # print(df['adjusted_coryat'].mean())
    # print(df.tail(10)['adjusted_coryat'].mean())
    # plt.figure(1)
    # df.adjusted_coryat.plot.hist()
    # plt.figure(2)
    # df.tail(10).adjusted_coryat.plot.hist()
    # plt.figure(3)
    df['rolling_final'].plot()
    plt.show()
