import platform
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Detectar sistema operativo con so
so = platform.system()

options = Options()

if so == "Windows":
    # Configuración para Windows con Chrome
    options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    service = Service(r"C:\chromedriver-win64\chromedriver.exe")

elif so == "Linux":
    # Configuración para Debian con Brave
    options.binary_location = "/usr/bin/brave-browser"
    service = Service("/usr/bin/chromedriver")

else:
    raise Exception(f"Sistema operativo no soportado: {so}")

driver = webdriver.Chrome(service=service, options=options)

driver.get("https://demoqa.com/text-box")
driver.maximize_window()
time.sleep(2)
nom = driver.find_element(By.CSS_SELECTOR, "#userName")
nom.send_keys("Rodrigo")
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, "#userEmail").send_keys("rodrigo@gmail.com")
time.sleep(1)
driver.find_element(By.XPATH, "//*[@id='currentAddress']").send_keys("Direccion uno")
time.sleep(1)
driver.find_element(By.XPATH, "//*[@id='permanentAddress']").send_keys("Direccion dos")
time.sleep(1)

driver.execute_script("window.scrollTo(0, 500)")
time.sleep(2)

driver.find_element(By.XPATH, "//*[@id='submit']").click()
time.sleep(2)


driver.close()