from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


    
@given('estando en el sitio web')
def step_impl(context):
    context.driver.get(context.config.get('URL', 'link'))
    
@when('estamos en la pagina principal')
def step_impl(context):
    pass
    
@then('cerrar sesion de perfil')
def step_impl(context):
    options =  context.driver.find_element(By.CSS_SELECTOR, 'a.nav-link.dropdown-toggle')
    options.click()
   
    

    # Encontrar y hacer clic en la tercera opción del menú desplegable
    third_option = context.driver.find_element(By.XPATH, '/html/body/div/div[1]/nav/div/div/div/div/div/a[3]')
    third_option.click()
    

    

