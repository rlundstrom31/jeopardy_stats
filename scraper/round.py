from scraper.category import Category

max_one_round_coryat = 18000

class Round:

    def __init__(self, round_number):
        self.adjusted_coryat = 0
        self.categories = list()
        self.round_number = round_number
        self.coryat = 0
        self.possible_coryat = 0
        self.num_correct = 0
        self.num_wrong = 0
        self.correct_daily_double = 0

    def scrape_round(self, driver):
        for i in range(1, 7):
            c = Category(self.round_number, i)
            c.scrape_category(driver)
            self.categories.append(c)
        for category in self.categories:
            self.coryat += category.coryat
            self.possible_coryat += category.possible_coryat
            self.num_correct += category.num_correct
            self.num_wrong += category.num_wrong
            self.correct_daily_double += category.correct_daily_double
        self.adjusted_coryat = self.round_number * self.coryat * max_one_round_coryat / self.possible_coryat
