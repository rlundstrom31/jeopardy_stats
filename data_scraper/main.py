import date_scraper
import game_scraper
import json
import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    # options.add_experimental_option("detach", True)
    # debugging help
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(options=options, service=service)
    email = os.environ['my_email']  # must set these using environmental variables
    password = os.environ['my_password']
    driver.get('https://www.j-scorer.com/login')
    driver.find_element(By.NAME, 'session[email]').send_keys(email)
    driver.find_element(By.NAME, 'session[password]').send_keys(password)
    driver.find_element(By.NAME, 'commit').click()
    # logging in complete - can start scraping games

    dates = date_scraper.date_scraper(driver)
    current_games = os.listdir("../games/")
    known_date_list = [None]*len(current_games)

    for i in range(len(current_games)):
        old_name = current_games[i]
        new_name = old_name[0:10]
        known_date_list[i] = new_name
    for date in dates:
        print(date)
        if date not in known_date_list:
            game = game_scraper.GameScraper(date)
            game.scrape_game(driver)
            with open("../games/" + str(date) + ".json", "w") as write_file:
                json.dump(game.__dict__, write_file)

    # element = driver.find_element(By.ID, 'topic-area-1')
    # print(element.get_attribute("value"))
