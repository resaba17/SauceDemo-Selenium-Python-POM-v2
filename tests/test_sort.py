from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
from utils.driver_setup import get_driver


def test_sort():
    driver = get_driver()

    try:
        driver.get("https://www.saucedemo.com/")

        login = LoginPage(driver)
        login.enter_username("standard_user")
        login.enter_password("secret_sauce")
        login.click_login()

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "product_sort_container")))

        dropdown = Select(
            driver.find_element(By.CLASS_NAME, "product_sort_container"))
        dropdown.select_by_visible_text("Price (low to high)")

        prices = driver.find_elements(By.CLASS_NAME, "inventory_item_price")
        values = [float(price.text.replace("$", "")) for price in prices]

        assert values == sorted(values)

    finally:
        driver.quit()
