import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
from utils.driver_setup import get_driver


def test_add_to_cart():
    driver = get_driver()

    try:
        driver.get("https://www.saucedemo.com/")

        login = LoginPage(driver)
        login.enter_username("standard_user")
        login.enter_password("secret_sauce")
        login.click_login()

        WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item")))

        buttons = driver.find_elements(By.XPATH,"//button[contains(text(),'Add to cart')]")

        selected = random.sample(buttons, 4)

        for button in selected:
            button.click()

        cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
        assert cart_badge.text == "4"

    finally:
        driver.quit()
