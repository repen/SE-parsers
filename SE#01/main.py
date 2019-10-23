'''
name: SE#01
author: Andrey Plugin
email: 9keepa@gmail.com
link: https://www.youtube.com/channel/UCNN3bpPlWWUkUMB7gjcUFlw
'''

from selenium import webdriver

driver = webdriver.Firefox()

driver.get("https://google.com")

screen = driver.get_screenshot_as_png()

with open("screen.png", "wb") as f:
    f.write(screen)