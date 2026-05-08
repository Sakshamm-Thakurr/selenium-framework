from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

class LoginPage:
    URL = "https://www.saucedemo.com"
    
    USERNAME_FIELD = (By.ID, "user-name")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CLASS_NAME, "error-message-container")
    INVENTORY_CONTAINER = (By.ID, "inventory_container")

    def __init__(self):
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.maximize_window()

    def open(self):
        self.driver.get(self.URL)

    def login(self, username, password):
        self.wait.until(EC.presence_of_element_located(self.USERNAME_FIELD)).send_keys(username)
        self.driver.find_element(*self.PASSWORD_FIELD).send_keys(password)
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def is_logged_in(self):
        try:
            self.wait.until(EC.presence_of_element_located(self.INVENTORY_CONTAINER))
            return True
        except:
            return False

    def get_error_message(self):
        try:
            return self.wait.until(EC.presence_of_element_located(self.ERROR_MESSAGE)).text
        except:
            return ""

    def quit(self):
        self.driver.quit()