import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.html
def test_itla_login():


    driver = webdriver.Chrome('C:\Drivers\chromedriver')

    # Entrar a la plataforma itla
    driver.get('https://plataformavirtual.itla.edu.do/login/index.php')
    driver.maximize_window()

    # Primera captura
    driver.save_screenshot('captura1.png')

    # Usuario y contraseña e ingresar las credenciales
    user_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, 'username'))
    )
    user_field.send_keys('20211132')

    password_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'password'))
    )
    password_field.send_keys('Detroyerd#1')

    # Hacer clic en el botón de inicio de sesión
    login_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'loginbtn'))
    )
    login_button.click()

    # Segunda captura
    driver.save_screenshot('captura2.png')

    # Cerrar el navegador
    driver.quit()






