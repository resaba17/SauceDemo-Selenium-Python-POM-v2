from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 

class LogoutPage:
    menu_button = (By.ID, "react-burger-menu-btn")
    logout_button = (By.ID, "logout_sidebar_link")

    def __init__(self, driver):
        self.driver = driver 
    def open_menu(self):
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(self.menu_button)).click() 
    def logout(self):
       WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(self.logout_button)).click() 