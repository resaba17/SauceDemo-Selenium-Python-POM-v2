from pages.login_page import LoginPage
from pages.checkout_page import CheckoutPage
from utils.driver_setup import get_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_complete_checkout():
    driver = get_driver()
    driver.get("https://www.saucedemo.com/")

    login = LoginPage(driver)
    login.enter_username("standard_user")
    login.enter_password("secret_sauce")
    login.click_login()

    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CLASS_NAME,"inventory_item")))

    driver.find_element(By.XPATH,"//button[contains(text(),'Add to cart')]").click()
    driver.find_element(By.CLASS_NAME,"shopping_cart_link").click()

    checkout = CheckoutPage(driver)
    checkout.click_checkout()
    checkout.enter_first_name("Resaba")
    checkout.enter_last_name("User")
    checkout.enter_postal_code("600001")
    checkout.click_continue()
    checkout.click_finish()

    assert checkout.get_success_message() == "Thank you for your order!"

    driver.quit()