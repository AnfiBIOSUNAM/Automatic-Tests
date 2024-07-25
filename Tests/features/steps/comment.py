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
    context.driver.get(context.config.get('URL', 'link'))
    
@when('Go to my shopping')
def step_impl(context):
    # Click on my profile button
    profile = context.driver.find_element(By.XPATH, "/html/body/div/div[1]/nav/div/div/div/div/a/img")
    profile.click()
    # Click on my shopping
    my_shopping = context.driver.find_element(By.XPATH, "/html/body/div/div[1]/nav/div/div/div/div/div/a[2]")
    my_shopping.click()
    
@when('Select the last element bought')
def step_impl(context):
    # Click on the last element bought
    table = context.driver.find_element(By.XPATH, "/html/body/div/div[1]/main/div[3]/div/table")
    rows = table.find_elements(By.TAG_NAME, "tr")
    assert len(rows) > 1, "The table is empty"
    
    last_product = rows[-1] # Get the las product, which is the last row
    
    try: # Click on the last row
        context.driver.execute_script("arguments[0].click();", last_product)
        print("Last row was clicked successfully.")
    except Exception as e:
        print(f"Failed to click on the last row: {e}")
    
@when('Comment the product')
def step_impl(context):
    context.product_commented = context.driver.find_element(By.XPATH, "/html/body/div/div[1]/main/section/div/div/div[2]/h1").text
    # Star the product
    stars = context.driver.find_elements(By.CLASS_NAME, "star")
    last_star = stars[-1] 
    actions = ActionChains(context.driver)
    actions.move_to_element(last_star).click().perform()
    # Fill the comment field
    comment = context.driver.find_element(By.XPATH, "/html/body/div/div[1]/main/section/div/div/div[2]/div[2]/textarea")
    comment.send_keys(context.config.get('Comment', 'comment'))
    # Click on the comment button
    context.driver.find_element(By.XPATH, "/html/body/div/div[1]/main/section/div/div/div[2]/button").click()
    
@then('Check if the product is commented')
def step_impl(context):
    # Go to see the products
    products_button = context.driver.find_element(By.XPATH, "/html/body/div/div[1]/nav/div/div/ul/li[2]/a")
    products_button.click()
    product = context.driver.find_element(By.XPATH ,f"//h3[text() = '{context.product_commented}']")
    if product:
        try: # Click on the last row
            context.driver.execute_script("arguments[0].click();", product)
            print("The product was clicked successfully.")
        except Exception as e:
            print(f"Failed to click on the last row: {e}")
        # Check if the comment is there
        comment_section = context.driver.find_element(By.XPATH, "/html/body/div/div[1]/main/section[2]/div/div[1]")
        comment_searched = comment_section.find_element(By.XPATH, f"//p[text() = '{context.config.get('Comment', 'comment')}']")
        assert comment_searched
    else:
        print("The product has been sold out")
        pass
    """wait = WebDriverWait(context.driver, 10)
    time.sleep(5)
    # Check if there is an h5 with the text "Excelente producto"
    h5 = context.driver.find_element(By.XPATH, "//h5[text()='Excelente producto']")
    assert h5"""