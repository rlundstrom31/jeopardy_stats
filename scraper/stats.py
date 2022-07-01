import json
import os

import pandas as pd
from matplotlib import pyplot as plt

from scraper.category import Category
from scraper.clue import Clue
from scraper.final import Final
from scraper.game import Game
from scraper.round import Round

if __name__ == '__main__':
    saved_games = os.listdir("../games/")
    games = set()
    for date in saved_games:
        with open("../games/" + str(date), "r") as read_file:
            game_data = json.load(read_file)
            game = Game('')
            for key in game_data.keys():
                game.__setattr__(key, game_data[key])
            rds = list()
            for i in range(2):
                r = Round(i+1)
                for key in game.rounds[i].keys():
                    r.__setattr__(key, game.rounds[i][key])
                cats = list()
                for j in range(6):
                    c = Category(i + 1, j + 1)
                    for key in r.categories[j].keys():
                        c.__setattr__(key, r.categories[j][key])
                    clues = list()
                    for k in range(5):
                        clue = Clue(i + 1, j + 1, k + 1, c.subjects)
                        for key in c.clues[k].keys():
                            clue.__setattr__(key, c.clues[k][key])
                        clues.append(clue)
                    c.__setattr__('clues', clues)
                    cats.append(c)
                r.__setattr__('categories', cats)
                rds.append(r)
            game.__setattr__('rounds', rds)
            f = Final()
            for key in game.final.keys():
                f.__setattr__(key, game.final[key])
            game.__setattr__('final', f)
            games.add(game)

    df = pd.DataFrame([(vars(game)) for game in games])
    df = df.drop(columns=['URL'])
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
    df3 = pd.DataFrame([vars(game.final) for game in games])
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
