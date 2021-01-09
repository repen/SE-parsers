'''
name: SE#03
author: Andrey Plugin
email: 9keepa@gmail.com
link: https://www.youtube.com/channel/UCNN3bpPlWWUkUMB7gjcUFlw

Copyright (c) 2019 - 2021 Andrey Plugin (9keepa@gmail.com)
Licensed under the MIT License https://github.com/repen/E-parsers/blob/master/License
'''

import time
from selenium import webdriver, common
from bs4 import BeautifulSoup #pip install bs4
from database import Database

WAIT = 2 

calendar_css = '.calendar__direction.calendar__direction--tomorrow'
match_css    = ".event__match.event__match--scheduled.event__match--oneLine"

driver = webdriver.Firefox()
driver.get("https://www.myscore.ru/")

elements = driver.find_elements_by_css_selector("div.tabs__tab")
elements[-1].click()


def find_matches(html):
    data = []
    url = "https://www.myscore.ru/match/{}/#match-summary"
    soup = BeautifulSoup(html, 'html.parser')
    matches = soup.select(match_css)

    for match in matches:
        id_match  = match["id"].split("_")[-1]
        url_match = url.format(id_match)
        data.append((id_match, url_match, 1))
    return data

def nexted(firefox):
    next_btn = firefox.find_element_by_css_selector(calendar_css)
    next_btn.click()
    time.sleep(WAIT)
    html = firefox.find_element_by_css_selector("div[id=live-table]").get_attribute("innerHTML")
    return html

def write_db(data):
    db = Database("/home/repente/prog/python/youtube/parsers/SE00/SE#03/myscore.db")
    db.write("INSERT INTO match VALUES (?,?,?)", data)

def load_db():
    pass


for _ in range(10):
    try:
        html = nexted(driver)
        matches = find_matches(html)
        write_db(matches)
    except common.exceptions.NoSuchElementException:
        print("End")
        break


driver.close()