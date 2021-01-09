'''
name: SE#02
author: Andrey Plugin
email: 9keepa@gmail.com
link: https://www.youtube.com/channel/UCNN3bpPlWWUkUMB7gjcUFlw

Copyright (c) 2019 - 2021 Andrey Plugin (9keepa@gmail.com)
Licensed under the MIT License https://github.com/repen/E-parsers/blob/master/License
'''

import time
from selenium import webdriver
from bs4 import BeautifulSoup #pip install bs4

driver = webdriver.Firefox()

driver.get("https://www.myscore.ru/")
time.sleep(2)
elements = driver.find_elements_by_css_selector("div.tabs__tab")
elements[1].click()

def track_matches(html):
    soup = BeautifulSoup(html, "html.parser")
    elements = soup.select(".event__match.event__match--live.event__match--oneLine")
    for element in elements:
        time_match = element.select_one("div.event__stage")
        goals = element.select_one("div.event__scores.fontBold")
        id_match = element["id"].split("_")[-1]

        if time_match and goals:
            time_match = time_match.text.strip()
            goals = goals.text.strip()
            if time_match.isdigit():
                time_match = int(time_match)
                total_goals = sum(list(map(lambda x:int(x.strip()), goals.split("-"))))
                urls = "https://www.myscore.ru/match/{}/#match-summary".format(id_match)
                if time_match > 50 and total_goals == 1:
                    print("{} min {} | {} | {}".format(time_match, total_goals, goals, urls))


temp_hash = 0
while True:
    html = driver.find_element_by_css_selector("div[id=live-table]").get_attribute("innerHTML")
    if temp_hash != hash(html):
        track_matches(html)
        temp_hash = hash(html)
    print("===================")
