from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By


class Final:

    def __init__(self):
        self.correct = False
        self.subjects = list()

    def scrape_final(self, driver):
        driver.find_element(By.XPATH, '/html/body/main/div[1]/div[2]/div[2]/div[3]/a').click()
        final_right = driver.find_element(By.ID, 'button-final-right')
        if final_right.get_attribute("class") == 'active':
            self.correct = True
        element = driver.find_element(By.XPATH, '/html/body/main/div[1]/div[1]/div[3]/input')
        subject_string = element.get_attribute('value')
        for subject in subject_string.split(", "):
            self.subjects.append(subject)
