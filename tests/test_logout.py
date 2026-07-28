from pages.login_page import LoginPage 
from pages.logout_page import LogoutPage 
from utils.driver_setup import get_driver 
from selenium.webdriver.support.ui import WebDriverWait

def test_logout():
    driver = get_driver()

    login = LoginPage(driver) 
    login.enter_username("standard_user")
    login.enter_password("secret_sauce")
    login.click_login() 

    logout = LogoutPage(driver) 
    logout.open_menu()
    logout.logout() 

    WebDriverWait(driver,10).until(lambda d: "saucedemo.com" in d.current_url.lower())

    assert "saucedemo.com" in driver.current_url.lower() 

    driver.quit() 