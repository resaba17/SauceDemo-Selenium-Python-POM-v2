from pages.login_page import LoginPage
from utils.driver_setup import get_driver 

def test_invalid_login():
    driver = get_driver() 
    
    login = LoginPage(driver)
    login.enter_username("invalid_user")
    login.enter_password("invalid_password")
    login.click_login() 

    assert "Epic sadface" in login.get_error_message()
    driver.quit() 