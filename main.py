import os
from dotenv import load_dotenv
from selenium_handler import seleniumGPT
from login import logIn
from chat_gpt_handler import chatGPTHandler


# Load variables from .env
load_dotenv()

selenium_gpt = seleniumGPT()
driver = selenium_gpt.start_driver("https://chat.openai.com/auth/login")

login_instance = logIn(driver, os.getenv('MAIL'), os.getenv('PASSWORD'))
correct_login = login_instance.login()

if correct_login:
    chat_gpt = chatGPTHandler(driver)
    result = chat_gpt.send_prompt("¿Qué tal estas?")

    print(result)

# result2 = chat_gpt.send_prompt("¿Me ayudas?")
#
# print(result2)