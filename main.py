import os
from dotenv import load_dotenv
from selenium_handler import seleniumGPT
from login import logIn
from chat_gpt_handler import chatGPTHandler


# Load variables from .env
load_dotenv()

# Load selenium driver
selenium_gpt = seleniumGPT()
driver = selenium_gpt.start_driver("https://chat.openai.com/auth/login")

#Login to chatgpt
login_instance = logIn(driver, os.getenv('MAIL'), os.getenv('PASSWORD'))
login_instance.usal_login()

#Send prompt1
chat_gpt = chatGPTHandler(driver)
result = chat_gpt.send_prompt("¿Qué tal estas?")

print(result)

#Send prompt2
result2 = chat_gpt.send_prompt("¿Me ayudas?")

print(result2)