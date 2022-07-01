from selenium.webdriver.common.by import By


class Clue:
    def __init__(self, round_number, category_number, clue_number, subjects):
        self.round_number = round_number
        self.category_number = category_number
        self.clue_number = clue_number
        self.subjects = subjects
        self.type = ''

    def scrape_clue(self, driver):
        self.type = driver.find_element(By.ID, 'clue-box-' +
                                        str(self.category_number) + '-' +
                                        str(self.clue_number)).get_attribute("class")[9:]