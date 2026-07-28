from pages.login_page import LoginPage
from pages.products_page import ProductsPage 
from utils.driver_setup import get_driver

def test_cart_icon():
    driver = get_driver()

    login = LoginPage(driver)
    login.enter_username("standard_user")
    login.enter_password("secret_sauce")
    login.click_login() 

    products = ProductsPage(driver) 

    assert products.is_cart_visible() 
    driver.quit() 