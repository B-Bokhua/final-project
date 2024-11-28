import pytest
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains

from src.Pages.admin_page import admin_page
from src.Pages.news_page import news_page
from src.utils.add_first_post import add_first_post
from src.utils.add_second_post import add_second_post
from src.utils.add_inactive_post import add_inactive_post
import csv


@pytest.fixture(scope="module")
def setup_driver():
    driver = webdriver.Chrome()
    driver.get("https://e-school.ge/?m=new&sm=new_new")
    driver.maximize_window()
    yield driver
    driver.quit()

def get_credentials(role):
    file_path = os.path.join(os.path.dirname(__file__), '../resources/login.csv')
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)


            for row in reader:
                if row[0] == role:
                    return row[1], row[2]
    except FileNotFoundError:
        raise FileNotFoundError(f"Could not find the file: {file_path}")
    raise ValueError(f"Role '{role}' not found in the file.")

def login_as_role(driver, role):
    email, password = get_credentials(role)
    username_field = driver.find_element(By.XPATH, '//*[@id="urname"]')
    password_field = driver.find_element(By.XPATH, '//*[@id="urpass"]')
    username_field.send_keys(email)
    password_field.send_keys(password)
    login_button = driver.find_element(By.XPATH, '//*[@value="ავტორიზაცია"]')
    login_button.click()
    time.sleep(2)


# def login_as_kids(driver):
#     username = driver.find_element(By.XPATH, '//*[@id="urname"]')
#     username.send_keys("kid4@gmail.com")
#     password = driver.find_element(By.XPATH, '//*[@id="urpass"]')
#     password.send_keys("123")
#     enter_button_1 = driver.find_element(By.XPATH, '//*[@value="ავტორიზაცია"]')
#     enter_button_1.click()
#     time.sleep(2)


def log_out(driver):
    profile_name = driver.find_element(By.XPATH, '//div[@class="header-profile-name"]')
    actions = ActionChains(driver)
    actions.move_to_element(profile_name).perform()
    time.sleep(2)

    logout_option = WebDriverWait(driver, 10).until(
        ec.element_to_be_clickable((By.XPATH, '/html/body/header/div[2]/div/div/nav/ul/li[3]')))
    logout_option.click()
    time.sleep(2)

    WebDriverWait(driver, 2).until(ec.presence_of_element_located((By.XPATH, '//*[@value="ავტორიზაცია"]')))

    time.sleep(2)


# def login_as_teacher(driver):
#     username = driver.find_element(By.XPATH, '//*[@id="urname"]')
#     username.send_keys("tap@gmail.com")
#     password = driver.find_element(By.XPATH, '//*[@id="urpass"]')
#     password.send_keys("123")
#     enter_button = driver.find_element(By.XPATH, '//*[@value="ავტორიზაცია"]')
#     enter_button.click()
#     time.sleep(2)

# def login_as_admin(driver):
#     username = driver.find_element(By.XPATH, '//*[@id="urname"]')
#     username.send_keys("tap@gmail.com")
#     password = driver.find_element(By.XPATH, '//*[@id="urpass"]')
#     password.send_keys("123")
#     enter_button = driver.find_element(By.XPATH, '//*[@value="ავტორიზაცია"]')
#     enter_button.click()
#     time.sleep(2)


# def login_as_parent(driver):
#     username = driver.find_element(By.XPATH, '//*[@id="urname"]')
#     username.send_keys("tap@gmail.com")
#     password = driver.find_element(By.XPATH, '//*[@id="urpass"]')
#     password.send_keys("123")
#     enter_button = driver.find_element(By.XPATH, '//*[@value="ავტორიზაცია"]')
#     enter_button.click()
#     time.sleep(2)

def navigate_kid_to_news_section(driver):
    news_section = WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[1]/nav/ul/li[11]/a')))
    news_section.click()
    time.sleep(2)

def navigate_teacher_to_news_section(driver):
    teacher_profile = driver.find_element(By.XPATH, '//*[@name="choose_teacher"]')
    teacher_profile.click()
    time.sleep(2)

    news_button = driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/nav/ul/li[10]/a/div[2]')
    news_button.click()
    time.sleep(2)

def navigate_admin_profile_to_news_section(driver):
    admin_page(driver)
    time.sleep(2)
    news_page(driver)



@pytest.mark.usefixtures("setup_driver")
def test_first_news_is_visible(setup_driver):
    add_first_post()
    driver = setup_driver

    login_as_role(driver, 'kid')
    navigate_kid_to_news_section(driver)

    visible_news = "პირველი სიახლე"
    visible_news_titles = [title.text for title in driver.find_elements(By.XPATH, '//h2[contains(text(), "პირველი სიახლე")]' )]

    assert visible_news in visible_news_titles, f"'{visible_news}' should be visible to kids!"
    log_out(driver)


first_post_old_style = ''
@pytest.mark.usefixtures("setup_driver")
def test_second_news_is_not_visible(setup_driver):
    global first_post_style

    driver = setup_driver
    login_as_role(driver, 'kid')
    navigate_kid_to_news_section(driver)
    first_post_style = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[1]/div/div/div[1]/a/div[1]').get_attribute('style')
    log_out(driver)

    add_second_post()

    login_as_role(driver, 'kid')
    navigate_kid_to_news_section(driver)

    hidden_news = "მეორე სიახლე"
    visible_news_titles = [title.text for title in driver.find_elements(By.CLASS_NAME, "news-title")]

    assert hidden_news not in visible_news_titles, f"'{hidden_news}' should NOT be visible to kids!"

    log_out(driver)

@pytest.mark.usefixtures("setup_driver")
def test_both_is_visible_for_teacher(setup_driver):
    driver = setup_driver

    login_as_role(driver, 'teacher')
    navigate_teacher_to_news_section(driver)

    first_news = "პირველი სიახლე"
    second_news = "მეორე სიახლე"

    first_news_title = [title.text for title in driver.find_elements(By.XPATH, '//h2[contains(text(), "პირველი სიახლე")]')]
    second_news_title = [title.text for title in driver.find_elements(By.XPATH, '//h2[contains(text(), "მეორე სიახლე")]')]

    assert first_news in first_news_title, f"'{first_news}' should be visible to the teacher!"
    assert second_news in second_news_title, f"'{second_news}' should be visible to the teacher!"

    log_out(driver)



def test_both_is_visible_for_admin(setup_driver):
    driver = webdriver.Chrome()
    driver.get("https://e-school.ge/?m=new&sm=new_new")
    driver.maximize_window()

    login_as_role(driver, 'admin')
    navigate_admin_profile_to_news_section(driver)
    time.sleep(3)

    first_news = "პირველი სიახლე"
    second_news = "მეორე სიახლე"

    time.sleep(2)

    first_news_title = [title.text for title in driver.find_elements(By.XPATH, '//h2[contains(text(), "პირველი სიახლე")]')]
    second_news_title = [title.text for title in driver.find_elements(By.XPATH, '//h2[contains(text(), "მეორე სიახლე")]')]

    assert first_news in first_news_title, f"'{first_news}' should be visible to the admin!"
    assert second_news in second_news_title, f"'{second_news}' should be visible to the admin!"

@pytest.mark.usefixtures("setup_driver")
def test_picture_title_text(setup_driver):
    driver = setup_driver

    login_as_role(driver, 'admin')
    navigate_admin_profile_to_news_section(driver)
    time.sleep(1)

    title_name = "მეორე სიახლე"
    text = "ახალი ამბავი მოხდა..."

    h2 = driver.find_element(By.XPATH, '//h2[contains(text(), "მეორე სიახლე")]')
    a_parent = h2.find_element(By.XPATH, '..')

    title_name_from_dom = driver.find_element(By.XPATH, '//h2[contains(text(), "მეორე სიახლე")]').text
    assert title_name_from_dom == title_name

    text_name_from_dom = driver.find_element(By.XPATH, '//p[contains(text(), "ახალი ამბავი მოხდა...")]').text
    assert text == text_name_from_dom

    image_dom = a_parent.find_element(By.XPATH, '//div[@class="news-listing-img"]')
    image_style_dom = image_dom.get_attribute("style")
    assert image_style_dom != first_post_old_style # this means that latest post image url has changed
    log_out(driver)

@pytest.mark.usefixtures("setup_driver")
def test_inactive_post(setup_driver):
    driver = setup_driver
    time.sleep(2)

    add_inactive_post()

    login_as_role(driver, 'admin')
    admin_profile = driver.find_element(By.XPATH, '//*[@name="choose_admin"]')
    admin_profile.click()

    time.sleep(3)
    driver.execute_script('window.scrollBy(0,200)')
    time.sleep(2)

    add_news_button = driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/nav/ul/li[18]/a')
    add_news_button.click()
    time.sleep(2)

    inactive_text = "არააქტიური"

    inactive_span_text = driver.find_element(By.XPATH,'//span[contains(text(), "არააქტიური")]').text
    assert inactive_text == inactive_span_text

    driver.quit()












