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

match_css    = ".event__match.event__match--scheduled.event__match--oneLine"
calendar_css = ".calendar__direction.calendar__direction--tomorrow"
WAIT = 2
PATH = "/home/repente/prog/python/youtube/parsers/SE00/SE#03/myscore.db"

# this code clicks all element at whom css selectors '.event__expander.icon--expander.expand'
js_script = '''
    (function(){
    	var elements = document.querySelectorAll(".event__expander.icon--expander.expand");
    	for (var i = elements.length - 1; i >= 0; i--) {
    		elements[i].click();
    	};
    })()
'''

def find_matches(html):
    data = []
    template = "https://www.myscore.ru/match/{}/#match-summary"
    soup = BeautifulSoup(html, 'html.parser')
    matches = soup.select(match_css)
    for match in matches:
        id_match = match['id'].split("_")[-1] #g_1_ 8hbUk4F4
        url = template.format(id_match)
        data.append( (id_match, url, 1) )
    return data

def nexted(firefox):
    next_btn = firefox.find_element_by_css_selector(calendar_css)
    next_btn.click()
    time.sleep(WAIT)

    firefox.execute_script(js_script)
    time.sleep(1)
    html = firefox.find_element_by_css_selector("div[id=live-table]").get_attribute("innerHTML")
    return html

def write_db(data):
    db = Database(PATH)
    db.write("INSERT INTO match VALUES(?,?,?)", data)

driver = webdriver.Firefox()
driver.get("https://www.myscore.ru/")

time.sleep(2)
elements = driver.find_elements_by_css_selector(".tabs__tab")

elements[-1].click()
html = driver.find_element_by_css_selector("div[id=live-table]").get_attribute("innerHTML")

matches = find_matches(html)
write_db(matches)
time.sleep(WAIT)

for _ in range(10):
    try:
        html = nexted(driver)
        matches = find_matches(html)
        write_db(matches)
    except common.exceptions.NoSuchElementException:
        print("End")
        driver.close()
        break





