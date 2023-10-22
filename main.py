from flask import Flask, request, jsonify
import os
from dotenv import load_dotenv
from selenium_handler import seleniumGPT
from login import logIn
from chat_gpt_handler import chatGPTHandler

app = Flask(__name__)

# Load variables from .env
load_dotenv()


@app.route('/chatgpt', methods=['POST'])
def chatgpt():
    prompt = request.json.get('prompt')

    selenium_gpt = seleniumGPT()
    driver = selenium_gpt.start_driver("https://chat.openai.com/auth/login")

    login_instance = logIn(driver, os.getenv('MAIL'), os.getenv('PASSWORD'))
    correct_login = login_instance.login()

    if correct_login:
        chat_gpt = chatGPTHandler(driver)
        result = chat_gpt.send_prompt(prompt)
        driver.quit()
        return jsonify({"response": result})
    else:
        driver.quit()
        return jsonify({"error": "Login failed"}), 401


if __name__ == '__main__':
    app.run(debug=True)


