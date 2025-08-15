import platform
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

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
print(f"Prueba en {so} - Navegador: {driver.capabilities['browserName']}")
print(driver.title)

driver.close()
driver.quit()
