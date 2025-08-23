import platform
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 

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
nom = driver.find_element(By.XPATH, "//input[@type='text' and @id='userName']")
nom.send_keys("Rodrigo")
nom.send_keys(Keys.TAB + "rodrigo@gmail.com" + Keys.TAB + "Direccion uno" + Keys.TAB + "Direccion dos " + Keys.TAB + Keys.ENTER)

driver.execute_script("window.scrollTo(0, 500)")
time.sleep(2)


driver.close()