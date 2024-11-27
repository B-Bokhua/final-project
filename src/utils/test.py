import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains

@pytest.fixture(scope="module")
def setup_driver():
    driver = webdriver.Chrome()
    driver.get("https://e-school.ge/?m=new&sm=new_new")
    driver.maximize_window()
    yield driver
    driver.quit()

def login_as_kids(driver):
    username = driver.find_element(By.XPATH, '//*[@id="urname"]')
    username.send_keys("kid4@gmail.com")
    password = driver.find_element(By.XPATH, '//*[@id="urpass"]')
    password.send_keys("123")
    enter_button_1 = driver.find_element(By.XPATH, '//*[@value="ავტორიზაცია"]')
    enter_button_1.click()
    time.sleep(2)

def log_out(driver):
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


def login_as_teacher(driver):
    username = driver.find_element(By.XPATH, '//*[@id="urname"]')
    username.send_keys("tap@gmail.com")
    password = driver.find_element(By.XPATH, '//*[@id="urpass"]')
    password.send_keys("123")
    enter_button = driver.find_element(By.XPATH, '//*[@value="ავტორიზაცია"]')
    enter_button.click()
    time.sleep(2)

def login_as_admin(driver):
    username = driver.find_element(By.XPATH, '//*[@id="urname"]')
    username.send_keys("tap@gmail.com")
    password = driver.find_element(By.XPATH, '//*[@id="urpass"]')
    password.send_keys("123")
    enter_button = driver.find_element(By.XPATH, '//*[@value="ავტორიზაცია"]')
    enter_button.click()
    time.sleep(2)


def login_as_parent(driver):
    username = driver.find_element(By.XPATH, '//*[@id="urname"]')
    username.send_keys("tap@gmail.com")
    password = driver.find_element(By.XPATH, '//*[@id="urpass"]')
    password.send_keys("123")
    enter_button = driver.find_element(By.XPATH, '//*[@value="ავტორიზაცია"]')
    enter_button.click()
    time.sleep(2)

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
    admin_profile = driver.find_element(By.XPATH, '//*[@name="choose_admin"]')
    admin_profile.click()

    driver.execute_script('window.scrollBy(0,200)')
    time.sleep(4)

    news_button = WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[1]/nav/ul/li[19]/a')))
    news_button.click()
    time.sleep(2)


@pytest.mark.usefixtures("setup_driver")
def test_first_news_is_visible(setup_driver):
    driver = setup_driver

    login_as_kids(driver)
    navigate_kid_to_news_section(driver)

    visible_news = "პირველი სიახლე"
    visible_news_titles = [title.text for title in driver.find_elements(By.XPATH, '/html/body/div[2]/div[2]/div/div[1]/div/div/div[1]/a/h2' )]

    assert visible_news in visible_news_titles, f"'{visible_news}' should be visible to kids!"

@pytest.mark.usefixtures("setup_driver")
def test_second_news_is_not_visible(setup_driver):
    driver = setup_driver

    login_as_kids(driver)
    navigate_kid_to_news_section(driver)

    hidden_news = "მეორე სიახლე"
    visible_news_titles = [title.text for title in driver.find_elements(By.CLASS_NAME, "news-title")]

    assert hidden_news not in visible_news_titles, f"'{hidden_news}' should NOT be visible to kids!"

@pytest.mark.usefixtures("setup_driver")
def test_both_is_visible_for_teacher(setup_driver):
    driver = setup_driver

    log_out(driver)

    login_as_teacher(driver)
    navigate_teacher_to_news_section(driver)

    first_news = "პირველი სიახლე"
    second_news = "მეორე სიახლე"

    first_news_title = [title.text for title in driver.find_elements(By.XPATH, '/html/body/div[2]/div[2]/div/div[1]/div/div/div[4]/a/h2')]
    second_news_title = [title.text for title in driver.find_elements(By.XPATH, '/html/body/div[2]/div[2]/div/div[1]/div/div/div[1]/a/h2')]

    assert first_news in first_news_title, f"'{first_news}' should be visible to the teacher!"
    assert second_news in second_news_title, f"'{second_news}' should be visible to the teacher!"


@pytest.mark.usefixtures("setup_driver")
def test_both_is_visible_for_admin(setup_driver):
    driver = setup_driver
    log_out(driver)

    login_as_admin(driver)
    navigate_admin_profile_to_news_section(driver)
    time.sleep(7)

    first_news = "პირველი სიახლე"
    second_news = "მეორე სიახლე"

    first_news_title = [title.text for title in driver.find_elements(By.XPATH, '/html/body/div[2]/div[2]/div/div[1]/div/div/div[4]/a/h2)')]
    second_news_title = [title.text for title in driver.find_elements(By.XPATH, '/html/body/div[2]/div[2]/div/div[1]/div/div/div[1]/a/h2')]

    assert first_news in first_news_title, f"'{first_news}' should be visible to the admin!"
    assert second_news in second_news_title, f"'{second_news}' should be visible to the admin!"






