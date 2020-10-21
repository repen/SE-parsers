from scraping import Scraping
from selenium import webdriver

# Scraping startup
scraping = Scraping()

# Selenium startup
driver = webdriver.Chrome("/home/repente/prog/python/youtube/parsers/SE00/SE#06/FlashscoreScraping/chromedriver")

# driver.get("https://ya.ru")
# # get all matches of Brazilian Championship Serie A 2019

scraping.collect(driver, 'brazil', 'serie-a', 2017)

# # get all LaLiga matches from 2012 until 2019
scraping.collect(driver, 'spain', 'laliga', 2018, 2012)

driver.quit()