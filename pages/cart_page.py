from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    REMOVE_BUTTONS = (By.XPATH, "//button[text()='Remove']")
    CONTINUE_SHOPPING = (By.ID, "continue-shopping")
    CART_ITEM_NAMES = (By.CLASS_NAME, "inventory_item_name")
    CART_ITEM_PRICES = (By.CLASS_NAME, "inventory_item_price")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_cart_items(self):
        try:
            return self.wait.until(EC.presence_of_all_elements_located(self.CART_ITEMS))
        except:
            return []

    def get_cart_item_count(self):
        return len(self.get_cart_items())

    def click_checkout(self):
        self.wait.until(EC.element_to_be_clickable(self.CHECKOUT_BUTTON)).click()

    def remove_first_item(self):
        buttons = self.wait.until(EC.presence_of_all_elements_located(self.REMOVE_BUTTONS))
        buttons[0].click()

    def get_item_names(self):
        items = self.wait.until(EC.presence_of_all_elements_located(self.CART_ITEM_NAMES))
        return [item.text for item in items]

    def continue_shopping(self):
        self.driver.find_element(*self.CONTINUE_SHOPPING).click()