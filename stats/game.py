class Game:

    def __init__(self,date):
        self.date = date
        self.URL = 'https://j-scorer.com/game?g=' + date
        self.coryat = 0
        self.first_round_coryat = 0
        self.second_round_coryat = 0
        self.possible_score = 0
        self.adjusted_coryat = 0
        self.num_correct = 0
        self.num_wrong = 0
        self.daily_double = 0
        self.final = False
        