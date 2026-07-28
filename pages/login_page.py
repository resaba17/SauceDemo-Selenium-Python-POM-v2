from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    username = (By.ID, "user-name")
    password = (By.ID, "password")
    login_button = (By.ID, "login-button") 
    error_message = (By.XPATH, "//h3[@data-test='error']")

    def __init__(self, driver):
     self.driver = driver
    def enter_username(self, username):
     WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.username)).send_keys(username) 
    def enter_password(self, password):
       WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.password)).send_keys(password)
    def click_login(self):
      WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.login_button)).click() 
    def get_error_message(self):
     return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.error_message)).text 