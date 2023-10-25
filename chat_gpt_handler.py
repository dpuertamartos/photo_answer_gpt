from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class chatGPTHandler:
    def __init__(self, driver):
        self.driver = driver

    def send_input(self, prompt):
        print("sending input")
        sleep(1)
        inputElement = WebDriverWait(self.driver, 90).until(EC.presence_of_element_located((By.TAG_NAME, "textarea")))
        inputElement.click()
        inputElement.send_keys(prompt)
        inputElement.send_keys(Keys.ENTER)

    def obtain_output(self):
        # Wait for the button with text "Regenerate" to appear
        WebDriverWait(self.driver, 90).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(., 'Regenerate')]")))

        # Now that the button has appeared, proceed to fetch the desired paragraphs
        outputElements = self.driver.find_elements(By.TAG_NAME, "p")

        results = []
        for element in outputElements:
            # Extract text from the paragraph
            text = element.text

            # Extract links from the paragraph
            links = element.find_elements(By.TAG_NAME, "a")
            link_urls = [link.get_attribute("href") for link in links]

            # Append text and links to results
            if text:
                results.append(text)
            if link_urls:
                results.extend(link_urls)

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







