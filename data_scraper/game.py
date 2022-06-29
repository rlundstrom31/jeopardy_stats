from selenium.webdriver.common.by import By

from data_scraper.final import Final
from data_scraper.round import Round

max_coryat = 54000

class Game:
    def __init__(self, date):
        self.date = date
        self.URL = 'https://j-scorer.com/game?g=' + date
        self.coryat = 0
        self.possible_coryat = 0
        self.num_correct = 0
        self.num_wrong = 0
        self.correct_daily_double = 0
        self.final = Final()
        self.rounds = list()

    def scrape_game(self, driver):
        """Scrapes the entire game.

           Keyword arguments:
           driver -- the current selenium driver that is being used to scrape. Must already be logged in.
           """

        driver.get(self.URL)
        round_one = Round(1)
        round_one.scrape_round(driver)
        self.rounds.append(round_one)
        driver.find_element(By.ID, 'round-two-link').click()
        round_two = Round(2)
        round_two.scrape_round(driver)
        self.rounds.append(round_two)
        self.final.scrape_final(driver)
        self.coryat = round_one.coryat + round_two.coryat
        self.possible_coryat = round_one.possible_coryat + round_two.possible_coryat
        self.num_correct = round_one.num_correct + round_two.num_correct
        self.num_wrong = round_one.num_wrong + round_two.num_wrong
        self.correct_daily_double = round_one.correct_daily_double + round_two.correct_daily_double
