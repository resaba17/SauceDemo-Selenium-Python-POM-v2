from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select 
import random 
from selenium.webdriver.support import expected_conditions as EC

class ProductsPage:

    add_to_cart_buttons = (By.XPATH, "//button[contains(text(),'Add to cart')]")
    cart_icon = (By.CLASS_NAME, "shopping_cart_link")
    sort_dropdown = (By.CLASS_NAME, "product_sort_container")

    product_cards = (By.CLASS_NAME, "inventory_item")
    product_name = (By.CLASS_NAME, "inventory_item_name")
    product_price = (By.CLASS_NAME, "inventory_item_price") 

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_first_product(self):
        self.wait.until(EC.element_to_be_clickable(self.add_to_cart_buttons)).click()

    def add_first_four_products(self):
        buttons = self.wait.until(EC.presence_of_all_elements_located(self.add_to_cart_buttons))

        for button in buttons[:4]:
            button.click()

    def open_cart(self):
        self.wait.until(EC.element_to_be_clickable(self.cart_icon)).click()

    def is_cart_visible(self):
        return self.wait.until(EC.visibility_of_element_located(self.cart_icon)).is_displayed()

    def sort_low_to_high(self):
        Select(self.wait.until(EC.element_to_be_clickable(self.sort_dropdown))).select_by_visible_text("Price (low to high)")

    def get_random_products(self):
        products = self.wait.until(EC.presence_of_all_elements_located(self.product_cards))
        return random.sample(products, 4) 

    def get_product_details(self, product):
        name = product.find_element(*self.product_name).text
        price = product.find_element(*self.product_price).text
        return name, price 