from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class CheckoutPage:

    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")
    ERROR_MESSAGE = (By.CLASS_NAME, "error-message-container")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "complete-header")
    SUMMARY_TOTAL = (By.CLASS_NAME, "summary_total_label")
    CANCEL_BUTTON = (By.XPATH, "//button[@id='cancel' or @class='btn_secondary back btn_medium']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def fill_info(self, first, last, postal):
        # Page load hone ka wait
        time.sleep(1)
        first_field = self.wait.until(EC.element_to_be_clickable(self.FIRST_NAME))
        first_field.clear()
        first_field.send_keys(first)
        self.driver.find_element(*self.LAST_NAME).send_keys(last)
        self.driver.find_element(*self.POSTAL_CODE).send_keys(postal)

    def click_continue(self):
        self.wait.until(EC.element_to_be_clickable(self.CONTINUE_BUTTON)).click()

    def click_finish(self):
        self.wait.until(EC.element_to_be_clickable(self.FINISH_BUTTON)).click()

    def get_error(self):
        try:
            return self.wait.until(EC.presence_of_element_located(self.ERROR_MESSAGE)).text
        except:
            return ""

    def get_success_message(self):
        try:
            return self.wait.until(EC.presence_of_element_located(self.SUCCESS_MESSAGE)).text
        except:
            return ""

    def get_total(self):
        try:
            return self.wait.until(EC.presence_of_element_located(self.SUMMARY_TOTAL)).text
        except:
            return ""

    def cancel(self):
        # Cart checkout page pe cancel button
        try:
            cancel = self.wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(text(),'Cancel')]")
            ))
            cancel.click()
        except:
            # Fallback
            self.driver.back()