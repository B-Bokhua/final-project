import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("https://e-school.ge/?m=new&sm=new_new")
driver.maximize_window()

username = driver.find_element(By.XPATH, '//*[@id="urname"]')
username.send_keys("kid4@gmail.com")
password = driver.find_element(By.XPATH, '//*[@id="urpass"]')
password.send_keys("123")
enter_button = driver.find_element(By.XPATH, '//*[@value="ავტორიზაცია"]')
enter_button.click()
time.sleep(3)

profile_name = driver.find_element(By.XPATH, '//div[@class="header-profile-name"]')
actions = ActionChains(driver)
actions.move_to_element(profile_name).perform()
time.sleep(2)

logout_option = WebDriverWait(driver, 10).until(
        ec.element_to_be_clickable((By.XPATH, '/html/body/header/div[2]/div/div/nav/ul/li[3]')))
logout_option.click()
time.sleep(2)

WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, '//*[@value="ავტორიზაცია"]')))

time.sleep(2)
driver.quit()