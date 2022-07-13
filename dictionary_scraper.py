"""
Simple webscraper used to get 4 letter words.
Writes out to a file named "word_bank.txt"
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


f = open("word_bank.txt", "a")
options = Options()
options.headless = True
options.add_argument("--window-size = 1920, 1200")


DRIVER_PATH = 'chromedriver'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get('https://eslforums.com/4-letter-words/')
all_words = driver.find_elements(By.TAG_NAME,'li' )
for word in all_words:
    text = word.text
    if (len(text) == 4):
        f.write(text + "\n")

driver.quit()
