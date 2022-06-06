import time
from datetime import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import requests
from bs4 import BeautifulSoup
from decouple import config


if __name__ == '__main__':

    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    email = config('email')
    password = config('password')
    driver.get('https://www.j-scorer.com/login')
    driver.find_element(By.NAME, 'session[email]').send_keys(email)
    driver.find_element(By.NAME, 'session[password]').send_keys(password)
    driver.find_element(By.NAME, 'commit').click()
    driver.get('https://j-scorer.com/game?g=2022-02-23')
    print(driver.find_element(By.ID, 'topic-area-1'))
    soup = BeautifulSoup(driver.page_source)
    print(soup.text)
    time.sleep(10)
