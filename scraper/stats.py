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
                r = Round(i + 1)
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
    df1 = pd.DataFrame([vars(game) for game in games])
    df1 = df1.drop(columns=['URL', 'final', 'rounds'])
    df1['date'] = pd.to_datetime(df1['date'])
    df1 = df1.sort_values('date')
    df1 = df1.reset_index()
    df1 = df1.drop(columns=['index'])
    df1 = df1.reset_index()
    df1 = df1.drop(columns=['index'])
    pd.set_option('display.max_columns', None)
    df3 = pd.DataFrame([(game.date, game.final.correct, game.final.subjects) for game in games])
    df3 = df3.rename(columns={0: 'date', 1: 'final_correctness', 2: 'final_subjects'})
    df3['date'] = pd.to_datetime(df3['date'])
    df3 = df3.sort_values('date')
    df3 = df3.reset_index()
    df3 = df3.drop(columns=['index'])
    print(df3)
    df = pd.concat([df1, df3], axis=1)
    df = df.loc[:, ~df.columns.duplicated()].copy()
    df['rolling_adjusted_coryat'] = df.adjusted_coryat.rolling(150).mean()
    df['rolling_final'] = df.final_correctness.rolling(150).mean()
    print(df)
    # print(df['adjusted_coryat'].mean())
    # print(df.tail(10)['adjusted_coryat'].mean())
    plt.figure(1)
    df.adjusted_coryat.plot()
    # plt.figure(2)
    # df.tail(10).adjusted_coryat.plot.hist()
    # plt.figure(3)
    # df['rolling_final'].plot()
    plt.show()
