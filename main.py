from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd
import time

def main():
    company = input("Please provide the instagram username of your corporate account: ")
    url = f'https://www.instagram.com/{company}'
    driver = Chrome()
    driver.get(url)
    # set up the options to webscrape 
    time.sleep(5)
    driver.close()
    posts = driver.find_elements(By.CLASS_NAME, "_aagu")
    print(posts)

if __name__ == '__main__':
    main()