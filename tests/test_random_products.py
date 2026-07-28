from pages.login_page import LoginPage 
from pages.products_page import ProductsPage
from utils.driver_setup import get_driver 

def test_random_products():
    driver = get_driver() 

    login = LoginPage(driver) 
    login.enter_username("standard_user")
    login.enter_password("secret_sauce")
    login.click_login()

    products = ProductsPage(driver) 

    selected_products = products.get_random_products() 

    assert len(selected_products) == 4 

    for product in selected_products:
        name, price = products.get_product_details(product)

        print(f"{name} - {price}")
    driver.quit() 