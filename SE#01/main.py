'''
name: SE#01
author: Andrey Plugin
email: 9keepa@gmail.com
link: https://www.youtube.com/channel/UCNN3bpPlWWUkUMB7gjcUFlw

Copyright 2019-2021 Andrey Plugin (9keepa@gmail.com)
Licensed under the Apache License v2.0
http://www.apache.org/licenses/LICENSE-2.0
'''

from selenium import webdriver

driver = webdriver.Firefox()

driver.get("https://google.com")
# screen = driver.get_screenshot_as_png()

# with open("screen.png", "wb") as f:
#     f.write(screen)