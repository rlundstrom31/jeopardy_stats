# things to calculate
# number right/wrong
# coryat / adjusted coryat
# for wayyy later - category breakdowns.
from selenium.webdriver.common.by import By

max_coryat = 54000


class GameScraper:

    def __init__(self, date):
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

    def scrape_game(self, driver):
        """Scrapes the entire game.

           Keyword arguments:
           driver -- the current selenium driver that is being used to scrape. Must already be logged in.
           """
        driver.get(self.URL)
        self.scrape_round(driver, 1)
        driver.find_element(By.ID, 'round-two-link').click()
        self.scrape_round(driver, 2)
        final_right = driver.find_element(By.ID, 'button-final-right')
        if final_right.get_attribute("class") == 'active':
            self.final = True
        self.adjusted_coryat = self.coryat * float(max_coryat)/self.possible_score
        #print(str(self.coryat) + ' first: ' + str(self.first_round_coryat) + ' second: ' +
              #str(self.second_round_coryat))
        print(self.date + ' adjusted coryat: ' + round(self.adjusted_coryat))
        # print(self.daily_double)
        # print(self.final)

    def scrape_round(self, driver, round_number):
        """Scrapes an individual round of the game.

           Keyword arguments:
           driver -- the current selenium driver that is being used to scrape. Must already be logged in.
           round_number -- 1 for single jeopardy, 2 for double jeopardy. Used to double the scores in double jeopardy.
           """
        round_coryat = 0
        for i in range(1, 7):
            for j in range(1, 6):
                clue = driver.find_element(By.ID, 'clue-box-' + str(i) + '-' + str(j)).get_attribute("class")
                clue = clue[9:]
                if clue != "clue-nr":
                    points = 200 * j * round_number
                    self.possible_score += points
                    if clue == "clue-right":
                        round_coryat += points
                        self.num_correct += 1
                    elif clue == "clue-wrong":
                        round_coryat -= points
                        self.num_wrong += 1
                    elif (clue == "dd-box clue-right") | (clue == "clue-right dd-box"):
                        round_coryat += points
                        self.daily_double += 1
        self.coryat += round_coryat
        if round_number == 1:
            self.first_round_coryat = round_coryat
        else:
            self.second_round_coryat = round_coryat

