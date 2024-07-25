from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

"""Feature: In the Website Prometienda add two products to the cart
    Scenario: Add to cart
    Given Open the Website
    When Go to the details of a product
    Then Select the quantity and add to cart"""
    
@given('Open the Website')
def step_impl(context):
    context.driver.get(context.config.get('URL', 'url'))
    
@when('Go to the details of a product')
def step_impl(context):
    # Get to the product details
    card = context.driver.find_element(By.XPATH, "/html/body/div/div[1]/main/section/div/div/div[1]/div/div[1]/img")
    card.click()
    
@when('Select the quantity and add to cart')
def step_impl(context):
    # Add 2 products
    context.driver.find_element(By.XPATH, "/html/body/div/div[1]/main/section[1]/div/div/div[2]/div[3]/button[2]").click()
    # Add to the cart
    context.driver.find_element(By.XPATH, "/html/body/div/div[1]/main/section[1]/div/div/div[2]/div[3]/button[3]").click()
    
@then('Check if the product is in the cart')
def step_impl(context):
    # Go to the cart
    context.driver.find_element(By.XPATH, "/html/body/div/div[1]/nav/div/div/div/li/a").click()
    # Check if there is an h5 with the text "Café"
    h5 = context.driver.find_element(By.XPATH, "//h5[text()='Café']")
    assert h5
    
