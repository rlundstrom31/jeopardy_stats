import json
import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from data_scraper import date_scraper
from data_scraper.game import Game



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

    # game scraping code
    dates = date_scraper.date_scraper(driver)
    current_games = os.listdir("../games/")
    known_date_list = [None]*len(current_games)

    for i in range(len(current_games)):
        old_name = current_games[i]
        new_name = old_name[0:10]
        known_date_list[i] = new_name
    for date in dates:
        if date not in known_date_list:
            print(date)
            game = Game(date)
            game.scrape_game(driver)
            with open("../games/" + str(date) + ".json", "w") as write_file:
                json.dump(game, write_file, default=lambda o: o.__dict__)