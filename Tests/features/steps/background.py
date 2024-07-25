from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#Acceder a la página
@given(u'quiero entrar a la pagina')
def step_impl(context):
    pass

@when(u'accedo a la pagina del proyecto')
def step_impl(context):
    context.driver.get(context.config.get("URL", "link"))

@then(u'validar entrada')
def step_impl(context):
    pass
    
#Hacer login
@given(u'quiero inlciar sesion')
def step_impl(context):
    pass
    
@when(u'estoy en la pagina de inicio')
def step_impl(context):
    pass

@then(u'dar click al boton')
def step_impl(context):
    time.sleep(2)
   
    button = context.driver.find_element(By.XPATH, "/html/body/div/div[1]/nav/div/div/ul/div/li[2]/a")
    button.click()
    

@then(u'llenar los datos y enviarlos')
def step_impl(context):
    correo = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.ID, "correo"))
    )
    correo.click()
    correo.send_keys("disneyplusdeal@gmail.com")
    
    password = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.ID, "contraseña"))
    )
    password.click()
    password.send_keys("123")

    button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.btn.btn-azul.mt-5[type="submit"]'))
    )
    context.driver.execute_script("arguments[0].scrollIntoView(true);", button)
    context.driver.execute_script("arguments[0].click();", button)
    

