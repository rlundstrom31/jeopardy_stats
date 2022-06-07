from selenium.webdriver.common.by import By

from selenium.webdriver.support.expected_conditions import staleness_of
from selenium.webdriver.support.wait import WebDriverWait


def date_scraper(driver):
    driver.get('https://www.j-scorer.com/stats')
    driver.find_element(By.ID, "ui-id-2").click()
    all_games = driver.find_element(By.ID, "show-all-games")
    if all_games is not None:
        all_games.click()
    date_list = list()
    # set up complete

    pages = int(driver.find_element(By.XPATH, '/html/body/main/div/div[2]/div[1]/div/nav/span[8]/a').text)

    for i in range(1, pages + 1):
        rows = 1 + len(driver.find_elements(By.XPATH, '/html/body/main/div/div[2]/div[1]/table/tbody/tr'))
        for r in range(1, rows):
            #TODO fix stale element issue
            WebDriverWait(driver, 10).until_not(staleness_of(driver.find_element(By.XPATH, '/html/body/main/div/div[2]/div[1]/table/tbody/tr[' + str(r) + ']/td[4]')))
            element = driver.find_element(By.XPATH, '/html/body/main/div/div[2]/div[1]/table/tbody/tr[' + str(r) + ']/td[4]')
            if element.text == 'regular play':
                WebDriverWait(driver, 10).until_not(staleness_of(element))
                date_list.append(element.text)
        if i != pages:
            page_length = len(driver.find_elements(By.XPATH, '/html/body/main/div/div[2]/div[1]/div/nav/span'))
            driver.find_element(By.XPATH,
                                '/html/body/main/div/div[2]/div[1]/div/nav/span[' + str(page_length) + ']/a').click()
    print(len(date_list))
    return date_list
