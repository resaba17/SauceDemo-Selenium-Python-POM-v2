from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
from utils.driver_setup import get_driver


def test_cart_details():
    driver = get_driver()

    try:
        driver.get("https://www.saucedemo.com/")

        login = LoginPage(driver)
        login.enter_username("standard_user")
        login.enter_password("secret_sauce")
        login.click_login()

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_item")))

        # Add first four products
        buttons = driver.find_elements(By.XPATH,"//button[contains(text(),'Add to cart')]")

        for button in buttons[:4]:
            button.click()

        # Open cart
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

        # Verify four items are present
        cart_items = driver.find_elements(By.CLASS_NAME, "cart_item")
        assert len(cart_items) == 4

    finally:
        driver.quit() 