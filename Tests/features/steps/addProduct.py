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
    pass
    #context.driver.find_element(By.XPATH, "//a[contains(text(),'Vestido de Noche')]").click()
    
@then('Select the quantity and add to cart')
def step_impl(context):
    pass
    #context.driver.find_element(By.ID, "quantity
    
