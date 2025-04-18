from selenium.webdriver.common.by import By

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver

    def add_to_cart(self):
        self.driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()

    def get_cart_count(self):
        return self.driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').text
