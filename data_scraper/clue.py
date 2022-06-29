from selenium.webdriver.common.by import By


class Clue:
    def __init__(self, round_number, category_number, clue_number, subjects, driver):
        self.clue_number = clue_number
        self.round_number = round_number
        self.subjects = subjects
        self.type = driver.find_element(By.ID, 'clue-box-' + str(category_number) + '-' + str(clue_number)).get_attribute("class")[9:]
        self.daily_double = False
