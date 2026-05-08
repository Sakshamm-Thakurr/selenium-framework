from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class InventoryPage:
    
    INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item")
    ADD_TO_CART_BUTTONS = (By.XPATH, "//button[text()='Add to cart']")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")
    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")
    ITEM_PRICES = (By.CLASS_NAME, "inventory_item_price")
    ITEM_NAMES = (By.CLASS_NAME, "inventory_item_name")
    REMOVE_BUTTONS = (By.XPATH, "//button[text()='Remove']")
    BURGER_MENU = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_all_items(self):
        return self.wait.until(EC.presence_of_all_elements_located(self.INVENTORY_ITEMS))

    def add_first_item_to_cart(self):
        buttons = self.wait.until(EC.presence_of_all_elements_located(self.ADD_TO_CART_BUTTONS))
        buttons[0].click()

    def add_all_items_to_cart(self):
        # Har baar fresh buttons fetch karo
        while True:
            buttons = self.driver.find_elements(*self.ADD_TO_CART_BUTTONS)
            if not buttons:
                break
            buttons[0].click()

    def get_cart_count(self):
        try:
            return int(self.wait.until(EC.presence_of_element_located(self.CART_BADGE)).text)
        except:
            return 0

    def go_to_cart(self):
        self.driver.find_element(*self.CART_ICON).click()

    def get_item_names(self):
        items = self.wait.until(EC.presence_of_all_elements_located(self.ITEM_NAMES))
        return [item.text for item in items]

    def get_item_prices(self):
        prices = self.wait.until(EC.presence_of_all_elements_located(self.ITEM_PRICES))
        return [float(p.text.replace("$", "")) for p in prices]

    def sort_by(self, value):
        from selenium.webdriver.support.ui import Select
        dropdown = self.wait.until(EC.presence_of_element_located(self.SORT_DROPDOWN))
        Select(dropdown).select_by_value(value)

    def logout(self):
        self.driver.find_element(*self.BURGER_MENU).click()
        time.sleep(0.8)  # Sidebar animation wait
        self.wait.until(EC.element_to_be_clickable(self.LOGOUT_LINK)).click()