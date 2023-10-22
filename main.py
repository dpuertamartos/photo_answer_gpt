from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import undetected_chromedriver as uc
from fake_useragent import UserAgent
import os
from dotenv import load_dotenv
from login import logIn

# Load variables from .env
load_dotenv()

op = webdriver.ChromeOptions()
# Your options setup
op.add_argument(f"user-agent={UserAgent().random}")
op.add_argument("user-data-dir=./")
op.add_experimental_option("detach", True)
op.add_experimental_option("excludeSwitches", ["enable-logging"])

driver = uc.Chrome(chrome_options=op)
driver.get("https://chat.openai.com/auth/login")

login_instance = logIn(driver, os.getenv('MAIL'), os.getenv('PASSWORD'))
login_instance.usal_login()

inputElements = driver.find_elements(By.TAG_NAME, "textarea")

i = 0
# while i<10:
inputElements[0].send_keys("Hola!, estoy probando")
sleep(2)
inputElements[0].send_keys(Keys.ENTER)
sleep(10)
inputElements = driver.find_elements(By.TAG_NAME, "p")
sleep(5)
results = []
for element in inputElements:
   results.append(element.text)
print(results)
i+=1
sleep(5)

driver.quit()