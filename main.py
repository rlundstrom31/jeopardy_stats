import os
import time
from datetime import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import game_scraper
import requests
from bs4 import BeautifulSoup


if __name__ == '__main__':
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(options = options, service=service)
    email = os.environ['my_email']
    password = os.environ['my_password']
    driver.get('https://www.j-scorer.com/login')
    driver.find_element(By.NAME, 'session[email]').send_keys(email)
    driver.find_element(By.NAME, 'session[password]').send_keys(password)
    driver.find_element(By.NAME, 'commit').click()
    game = game_scraper.GameScraper('https://j-scorer.com/game?g=2022-02-24')
    game.scrape_game(driver)



    # element = driver.find_element(By.ID, 'topic-area-1')
    # print(element.get_attribute("value"))
