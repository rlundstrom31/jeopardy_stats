import json
import os

import pandas as pd
from matplotlib import pyplot as plt

from scraper.game import Game

if __name__ == '__main__':
    saved_games = os.listdir("../games/")
    games = set()
    for date in saved_games:
        with open("../games/" + str(date), "r") as read_file:
            game_data = json.load(read_file)
            game = Game('')
            for key in game_data.keys():
                game.__setattr__(key, game_data[key])
            games.add(game)
    df = pd.DataFrame([vars(game) for game in games])
    df = df.drop(columns=['URL', 'final', 'rounds'])
    df['date'] = pd.to_datetime(df['date'])
    df = df.sort_values('date')
    df = df.reset_index()
    df = df.drop(columns=['index'])

    df['rolling_adjusted_coryat'] = df.adjusted_coryat.rolling(30).mean()
    # df['rolling_final'] = df.final.rolling(25).mean()
    df = df.reset_index()
    df = df.drop(columns=['index'])
    pd.set_option('display.max_columns', None)
    print(df)
    temp = list()
    for game in games:
        temp2 = list()
        temp2.append(game.date)
        for a in game.final:
            temp2.append(a)
        temp.append(temp2)
    df2 = pd.DataFrame([[game.date, [a for a in game.final]] for game in games])
    print(df2)
    df3 = pd.DataFrame([game.final for game in games])
    print(df3)
    # print(df['adjusted_coryat'].mean())
    # print(df.tail(10)['adjusted_coryat'].mean())
    # plt.figure(1)
    # df.adjusted_coryat.plot.hist()
    # plt.figure(2)
    # df.tail(10).adjusted_coryat.plot.hist()
    # plt.figure(3)
    # df['rolling_final'].plot()
    plt.show()