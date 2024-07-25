from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

"""Feature: Add a comment
    Scenario: Comment a product
    Given We are in the website
    When Go to my shopping
    When Select the last element bought
    when Comment the product
    Then Check if the product is commented"""
    
@given('We are in the website')
def step_impl(context):
    context.driver.get(context.config.get('URL', 'url'))
    
@when('Go to my shopping')
def step_impl(context):
    # Click on the login button
    context.driver.find_element(By.XPATH, "/html/body/div/div[1]/nav/div/div/ul/div/li[3]/a").click()
    
@when('Select the last element bought')
def step_impl(context):
    # Click on the last element bought
    context.driver.find_element(By.XPATH, "/html/body/div/div[1]/main/section/div/div/div[1]/div/div[1]").click()
    
@when('Comment the product')
def step_impl(context):
    # Fill the comment field
    comment = context.driver.find_element(By.ID, "comentario")
    comment.send_keys("Excelente producto")
    # Click on the comment button
    context.driver.find_element(By.XPATH, "/html/body/div/div[1]/main/section/div/div/div[2]/form/button").click()
    
@then('Check if the product is commented')
def step_impl(context):
    wait = WebDriverWait(context.driver, 10)
    time.sleep(5)
    # Check if there is an h5 with the text "Excelente producto"
    h5 = context.driver.find_element(By.XPATH, "//h5[text()='Excelente producto']")
    assert h5