from selenium import webdriver


driver = webdriver.Firefox()

driver.get("https://www.google.com")
screenshot = driver.get_screenshot_as_png()
with open("file.png", "wb") as f:
    f.write(screenshot)