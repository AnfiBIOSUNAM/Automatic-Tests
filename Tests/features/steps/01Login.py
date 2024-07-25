from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


"""Feature: Open Prometienda
    Scenario: Open the Website
    Given The website is opened
    When Do the login
    Then We are in home"""
    
@given('The website is opened')
def step_impl(context):
    context.driver.get(context.config.get('URL', 'url'))
    
@when('Do the login')
def step_impl(context):
    # Click on the login button
    context.driver.find_element(By.XPATH, "/html/body/div/div[1]/nav/div/div/ul/div/li[2]/a").click()
    # Fill the email field
    email = context.driver.find_element(By.ID, "correo")
    email.send_keys(context.config.get('User', 'email'))
    # Fill the password field
    password = context.driver.find_element(By.ID, "contraseña")
    password.send_keys(context.config.get('User', 'password'))
    
@then('We are in home')
def step_impl(context):
    # Click on the login button
    context.driver.find_element(By.XPATH, "/html/body/div/div[1]/main/form/fieldset/div[3]/button").click()
    # Check if the user is logged in
    h1 = context.driver.find_element(By.XPATH, "//p[text()='Tu tienda virtual de la Facultad de Ciencias']")
    assert h1