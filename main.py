from selenium import webdriver
import undetected_chromedriver as uc
from fake_useragent import UserAgent
import os
from dotenv import load_dotenv
from login import logIn
from chat_gpt_handler import chatGPTHandler

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

chat_gpt = chatGPTHandler(driver)
result = chat_gpt.send_prompt("¿Qué tal estas?")

print(result)

result2 = chat_gpt.send_prompt("¿Me ayudas?")

print(result2)