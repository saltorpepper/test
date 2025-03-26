#Sauce Demo

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

# Initialize WebDriver
driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/v1/")
driver.maximize_window()
print(driver.current_url)

def login():
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

def add_random_products():
    products = driver.find_elements(By.CLASS_NAME, "inventory_item")
    num_products = random.randint(1, len(products))
    selected_products = random.sample(products, num_products)
    
    for product in selected_products:
        product.find_element(By.TAG_NAME, "button").click()
    return num_products

def validate_cart_icon(expected_count):
    cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    assert int(cart_badge) == expected_count, "Cart count mismatch"

def go_to_cart():
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

def validate_cart_items():
    cart_items = driver.find_elements(By.CLASS_NAME, "cart_item")
    assert len(cart_items) > 0, "No items in cart"

def checkout():
    wait = WebDriverWait(driver, 15)
    # print(driver.page_source)
    

    print("Current URL:", driver.current_url)
    wait = WebDriverWait(driver, 15)
    checkout_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "checkout_button")))
    checkout_button = driver.find_element(By.CLASS_NAME, "checkout_button")
    checkout_button.click()
    driver.find_element(By.ID, "first-name").send_keys("Test")
    driver.find_element(By.ID, "last-name").send_keys("User")
    driver.find_element(By.ID, "postal-code").send_keys("12345")
    driver.find_element(By.ID, "continue").click()
    print(driver.page_source)

def validate_total():
    item_prices = driver.find_elements(By.CLASS_NAME, "inventory_item_price")
    total_price = sum(float(price.text.replace("$", "")) for price in item_prices)
    displayed_total = driver.find_element(By.CLASS_NAME, "summary_subtotal_label").text
    displayed_total_value = float(displayed_total.split("$")[-1])
    assert abs(total_price - displayed_total_value) < 0.01, "Total price mismatch"

# Execute test steps
login()
time.sleep(2)

num_products_added = add_random_products()
time.sleep(2)

validate_cart_icon(num_products_added)
go_to_cart()
time.sleep(2)

validate_cart_items()
checkout()
time.sleep(2)

validate_total()

driver.quit()
print("Smoke test passed successfully!")
