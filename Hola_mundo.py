from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.ie.service import Service

service = Service(r"C:\chromedriver-win64\chromedriver.exe")

driver = webdriver.Chrome(service=service)

driver.get("https://demoqa.com/text-box")
print("bienvendio a selenium")
print(driver.title)

driver.close()