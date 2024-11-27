import time
from selenium.webdriver.common.by import By


def news_page(driver):
    driver.execute_script('window.scrollBy(0,200)')
    time.sleep(2)
    news_button = driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/nav/ul/li[19]/a')
    news_button.click()
    time.sleep(2)