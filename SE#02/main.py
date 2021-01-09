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

def track_matches(container):
    soup = BeautifulSoup(container, "html.parser")
    matches = soup.select(".event__match.event__match--live.event__match--oneLine")
    for match in matches:
        time_match = match.select_one("div.event__stage--block")
        total = match.select_one("div.event__scores.fontBold")
        id_match = match["id"].split("_")[-1] # g_1_ b9HDyRiE

        if time_match and total:
            time_match = time_match.text.strip()
            total = total.text.strip()
            if time_match.isdigit():
                time_match = int(time_match)
                total_sum = sum(list(map(lambda x : int(x.strip()), total.split("-"))))
                url = "https://www.myscore.com.ua/match/{}/#match-summary".format(id_match)
                if time_match > 70 and total_sum < 3:
                    print(time_match, total_sum, total, url)



temp_hash = 0
while True:
    container = driver.find_element_by_css_selector("div[id=live-table]").get_attribute("innerHTML")
    if temp_hash != hash(container):
        track_matches(container)
        temp_hash = hash(container)
        print("=================================")
    time.sleep(2)



