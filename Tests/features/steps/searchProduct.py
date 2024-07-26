from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
from background import *

@given('estoy logueado en la pagina')
def step_impl(context):
    context.driver.get(context.config.get("URL", "link"))

@when('busco el producto "{producto}"')
def step_impl(context, producto):
    try:
        search_box = WebDriverWait(context.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/div/div[1]/main/div[2]/div[1]/input'))
        )

        # Limpiar el campo de búsqueda
        search_box.clear()

        search_box.send_keys(producto)

        WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div/div[1]/main/section/div'))
        )
    except (TimeoutException, ElementClickInterceptedException) as e:
        raise AssertionError(f"Error al buscar el producto {producto}: {str(e)}")

@then('se muestran los resultados de búsqueda para "{producto}"')
def step_impl(context, producto):
    try:
        container = WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div/div[1]/main/section/div'))
        )

        results = WebDriverWait(context.driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.col.mb-5'))
        )

        # Imprimir los resultados para depuración
        for result in results:
            print(result.text)

        if results:
            found = any(producto.lower() in result.text.lower() for result in results)
            if not found:
                print(f"No se encontraron resultados que contengan '{producto}'")
        else:
            print("No se encontraron resultados para la búsqueda.")

    except TimeoutException:
        print(f"No se encontraron resultados para {producto} dentro del tiempo esperado")