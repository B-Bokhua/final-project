import time
from selenium.webdriver.common.by import By


def add_news_page(driver):
    add_news = driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/nav/ul/li[18]/a/div[2]')
    add_news.click()
    time.sleep(3)
