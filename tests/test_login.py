import pytest 
from data.test_data import LOGIN_DATA 
from utils.driver_setup import get_driver
from pages.login_page import LoginPage 
from selenium.webdriver.support.ui import WebDriverWait

@pytest.mark.parametrize("username, password", LOGIN_DATA) 
def test_valid_login(username, password):
    driver = get_driver() 

    driver.get("https://www.saucedemo.com/")

    login = LoginPage(driver)
    login.enter_username(username)
    login.enter_password(password)
    login.click_login()

    WebDriverWait(driver,10).until(lambda d: "inventory" in d.current_url.lower())

    assert "inventory" in driver.current_url.lower()
    driver.quit() 