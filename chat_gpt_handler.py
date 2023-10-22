from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class chatGPTHandler:
    def __init__(self, driver):
        self.driver = driver

    def send_input(self, prompt):

        sleep(1)
        #remove popup if exist
        try:
            popup = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div/div[1]/button/svg/line[2]")
            popup.click()
        except:
            pass

        inputElements = self.driver.find_elements(By.TAG_NAME, "textarea")
        inputElements[0].click()
        inputElements[0].send_keys(prompt)
        sleep(1)
        inputElements[0].send_keys(Keys.ENTER)

    def obtain_output(self):
        # Wait for the button with text "Regenerate" to appear
        WebDriverWait(self.driver, 90).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(., 'Regenerate')]")))

        # Now that the button has appeared, proceed to fetch the desired paragraphs
        outputElements = self.driver.find_elements(By.TAG_NAME, "p")

        results = []
        for element in outputElements:
            results.append(element.text)

        #Clean array of "ChatGPT" non desired text
        if results and results[-1] == "ChatGPT":
            results.pop()

        return "\n".join(results)

    def send_prompt(self, prompt):
        '''
        :param prompt: String
        :return output: String
        '''
        self.send_input(prompt)
        return self.obtain_output()







