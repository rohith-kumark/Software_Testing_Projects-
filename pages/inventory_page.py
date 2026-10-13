from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    PAGE_TITLE = (By.CLASS_NAME, "title")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def is_loaded(self) -> bool:
        try:
            self.wait.until(EC.url_contains("inventory.html"))
            title = self.driver.find_element(*self.PAGE_TITLE).text
            return title == "Products"
        except Exception:
            return False
