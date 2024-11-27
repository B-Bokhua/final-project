from selenium.webdriver.common.by import By


def admin_page(driver):
    admin_profile = driver.find_element(By.XPATH, '//*[@name="choose_admin"]')
    admin_profile.click()