import pytest        
from loginpage import LoginPage
from Inventary import InventoryPage

def test_login_and_add_to_cart(setup):
    driver = setup
    driver.get("https://www.saucedemo.com/")

    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")

    inventory = InventoryPage(driver)
    inventory.add_to_cart()

    assert inventory.get_cart_count() == "1"
