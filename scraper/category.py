import time

from selenium.webdriver.common.by import By

from scraper.clue import Clue

max_one_category_coryat = 3000


class Category:

    def __init__(self, round_number, category_number):
        self.adjusted_coryat = 0
        self.round_number = round_number
        self.category_number = category_number
        self.subjects = list()
        self.clues = list()
        self.coryat = 0
        self.possible_coryat = 0
        self.num_correct = 0
        self.num_wrong = 0
        self.daily_double = 0
        self.correct_daily_double = 0

    def scrape_category(self, driver):
        subject_string = ''
        while subject_string == '':
            time.sleep(1)
            element = driver.find_element(By.ID, 'topic-area-' + str(self.category_number))
            subject_string = element.get_attribute('value')
        for subject in subject_string.split(", "):
            self.subjects.append(subject)
        for j in range(1, 6):
            clue = Clue(self.round_number, self.category_number, j, self.subjects)
            clue.scrape_clue(driver)
            if clue.type != "clue-nr":
                points = 200 * j * self.round_number
                self.possible_coryat += points
                if clue.type == "clue-right":
                    self.coryat += points
                    self.num_correct += 1
                elif clue.type == "clue-wrong":
                    self.coryat -= points
                    self.num_wrong += 1
                elif (clue.type == "dd-box clue-right") | (clue.type == "clue-right dd-box"):
                    self.coryat += points
                    self.daily_double += 1
                    self.correct_daily_double += 1
                elif (clue.type == "dd-box clue-pass") | (clue.type == "clue-pass dd-box"):
                    self.daily_double += 1
            self.clues.append(clue)
        self.adjusted_coryat = self.round_number * self.coryat * max_one_category_coryat / self.possible_coryat
