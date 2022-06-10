import time

from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


def date_scraper(driver):
    wait = WebDriverWait(driver, 10)
    driver.get('https://www.j-scorer.com/stats')
    driver.find_element(By.ID, "ui-id-2").click()
    all_games = driver.find_element(By.ID, "show-all-games")
    if all_games is not None:
        all_games.click()
    time.sleep(1)
    date_list = list()
    # set up complete

    pages = int(driver.find_element(By.XPATH, '/html/body/main/div/div[2]/div[1]/div/nav/span[8]/a').text)

    for i in range(1, pages + 1):
        soup = BeautifulSoup(driver.page_source, features="html.parser")
        for row in soup.main.find(id="games").div.tbody.find_all("tr"):
            row_list = row.find_all("td")
            show_type = row_list[3].text
            if show_type == 'regular play':
                date_list.append(str(row_list[2].text))
        if i != pages:
            page_length = len(driver.find_elements(By.XPATH, '/html/body/main/div/div[2]/div[1]/div/nav/span'))
            driver.find_element(By.XPATH,
                                '/html/body/main/div/div[2]/div[1]/div/nav/span[' + str(page_length) + ']/a').click()
        print(len(date_list))
        time.sleep(1)
    print(date_list)
    print(len(date_list))
    return date_list
