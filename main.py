import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

import date_scraper
import game_scraper

if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(options=options, service=service)
    email = os.environ['my_email']  # must set these yourself using environmental variables
    password = os.environ['my_password']
    driver.get('https://www.j-scorer.com/login')
    driver.find_element(By.NAME, 'session[email]').send_keys(email)
    driver.find_element(By.NAME, 'session[password]').send_keys(password)
    driver.find_element(By.NAME, 'commit').click()
    # logging in now complete - can start scraping games

    dates = date_scraper.date_scraper(driver)
    # for date in dates:
    #     game = game_scraper.GameScraper(date)
    #     game.scrape_game(driver)

    # element = driver.find_element(By.ID, 'topic-area-1')
    # print(element.get_attribute("value"))
