from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as ec

def add_first_post():
    driver = webdriver.Chrome()
    driver.get("https://e-school.ge/?m=new&sm=new_new")
    driver.maximize_window()
    time.sleep(2)

    username = driver.find_element(By.XPATH, '//*[@id="urname"]')
    username.send_keys("tap@gmail.com")
    password = driver.find_element(By.XPATH, '//*[@id="urpass"]')
    password.send_keys("123")
    enter_button = driver.find_element(By.XPATH, '//*[@value="ავტორიზაცია"]')
    enter_button.click()
    time.sleep(2)

    admin_profile = driver.find_element(By.XPATH, '//*[@name="choose_admin"]')
    admin_profile.click()
    time.sleep(3)

    # assert "dashboard" in driver.current_url or "admin" in driver.page_source, "Login failed!"

    driver.execute_script('window.scrollBy(0,200)')
    time.sleep(2)

    add_news = driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/nav/ul/li[18]/a/div[2]')
    add_news.click()
    time.sleep(3)

    add_news_button = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/div/a')
    add_news_button.click()
    time.sleep(3)

    #სიახლე 1
    title_1 = driver.find_element(By.XPATH, '//*[@id="title"]')
    title_1.send_keys("პირველი სიახლე")
    time.sleep(2)

    type_dropdown_1 = Select(WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.NAME, "type"))))
    type_dropdown_1.select_by_index(0)
    time.sleep(2)

    audience_dropdown_1 = Select(WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.NAME, "audience"))))
    audience_dropdown_1.select_by_index(5)
    time.sleep(2)


    publish_date_field_1 = WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.NAME, "publish_date")))
    publish_date_field_1.send_keys("11-25-2024")
    time.sleep(2)

    cancellation_date_field_1 = WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.NAME, "unpublish_date")))
    cancellation_date_field_1.send_keys('01-24-2025')
    time.sleep(2)


    text_field_1 = driver.find_element(By.XPATH, '//*[@id="quill-editor-news"]/div[1]')
    text_field_1.send_keys("ახალი ამბავი მოხდა 1")
    time.sleep(2)

    image_upload_1 = WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.NAME, "image")))
    image_path = '/Users/apple/Desktop/e-school/სიახლე 1.jpg'
    image_upload_1.send_keys(image_path)
    time.sleep(2)

    submit_button = WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.CLASS_NAME, "submit-button")))
    submit_button.click()
    time.sleep(2)

    driver.quit()
