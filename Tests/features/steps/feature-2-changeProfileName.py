from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('Estamos en la página de inicio')
def step_given_we_are_on_homepage(context):
    context.driver.get(context.config.get('URL', 'link'))  

@when('Navegar a la sección del perfil')
def step_when_navigate_to_profile_page(context):
    wait = WebDriverWait(context.driver, 10)
    profile_image = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'img.imagen-perfil')))
    profile_image.click()
    profile_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.dropdown-item[href="/perfil"]')))
    profile_link.click()

@when('Edito el nombre a "Anonimo"')
def step_when_edit_name(context):
    wait = WebDriverWait(context.driver, 10)
    edit_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'i.bi-pencil')))
    edit_button.click()
    name_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[name="nombre"]')))
    name_input.clear()
    name_input.send_keys('Anonimo')

@when('Guardo el nombre')
def step_when_save_name(context):
    wait = WebDriverWait(context.driver, 10)
    save_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.btn-azul')))
    save_button.click()

@then('Verificar el nombre "Anonimo" en la pagina')
def step_impl(context):
    wait = WebDriverWait(context.driver, 10)
    profile_name = wait.until(EC.text_to_be_present_in_element((By.XPATH, '/html/body/div/div[1]/main/div/div[2]/span'), 'Anonimo'))
    assert profile_name, f'Esperado "Anonimo", pero se encontró "{profile_name}"'
    
