from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.expected_conditions import presence_of_element_located, staleness_of
from selenium.webdriver.support.wait import WebDriverWait


def date_scraper(driver):
    driver.get('https://www.j-scorer.com/stats')
    driver.find_element(By.ID, "ui-id-2").click()
    all_games = driver.find_element(By.ID, "show-all-games")
    if all_games is not None:
        all_games.click()
    date_list = list()
    #set up complete

    #code to scrape one page
    #TODO: Add a loop that handles multiple pages
    rows = 1 + len(driver.find_elements(By.XPATH, '/html/body/main/div/div[2]/div[1]/table/tbody/tr'))
    for r in range(1,rows):
        WebDriverWait(driver,10).until_not(staleness_of(driver.find_element(By.XPATH, '/html/body/main/div/div[2]/div[1]/table/tbody/tr[' + str(r) + ']/td[4]')))
        time.sleep(0.001) #jank but it works?
        if driver.find_element(By.XPATH, '/html/body/main/div/div[2]/div[1]/table/tbody/tr[' + str(r) + ']/td[4]').text == 'regular play':
            date_list.append(driver.find_element(By.XPATH, '/html/body/main/div/div[2]/div[1]/table/tbody/tr[' + str(r) + ']/td[3]').text)
    print(len(date_list))
    print(date_list)