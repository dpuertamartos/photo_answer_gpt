from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class logIn:

    def __init__(self, driver, mail, password):
        self.driver = driver
        self.mail = mail
        self.password = password

    def usal_login(self):
        #wait for log in button
        page_load_wait = WebDriverWait(self.driver, 20)
        log_in = page_load_wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[1]/div/div/button[1]")))
        log_in.click()

        #wait for google log in button
        google_log_wait = WebDriverWait(self.driver, 20)
        google_log_in_button = google_log_wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/main/section/div/div/div/div[4]/form[2]/button/span[2]')))
        google_log_in_button.click()

        #fill google email and press next
        google_form_wait = WebDriverWait(self.driver, 20)
        mail = google_form_wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input")))
        mail.send_keys(self.mail)
        next_btn_google = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[2]/div/div[1]/div/div/button/span")[0]
        next_btn_google.click()

        #usal login
        usal_wait = WebDriverWait(self.driver, 20)
        send_usal_credential = usal_wait.until(EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div/div[2]/div[3]/div[1]/div[1]/div[1]/div[1]/form/div[2]/div[2]/input")))
        user_usal = self.driver.find_element(By.XPATH,
                                             "/html/body/div/div[2]/div[3]/div[1]/div[1]/div[1]/div[1]/form/div[1]/input")
        user_usal.send_keys(self.mail.replace("@usal.es", ""))

        password = self.driver.find_element(By.XPATH,
                                            "/html/body/div/div[2]/div[3]/div[1]/div[1]/div[1]/div[1]/form/div[2]/div[1]/input")
        password.send_keys(self.password)
        send_usal_credential.click()

        # continue google check
        try:
            continue_google_wait = WebDriverWait(self.driver, 15)
            continue_button = continue_google_wait.until(EC.element_to_be_clickable((By.XPATH,
                                                                                     "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span")))
            continue_button.click()
        except TimeoutException:
            print("Continue button not found. Skipping...")

        # lets_go chat gpt button
        try:
            letsgo_wait = WebDriverWait(self.driver, 15)
            letsgo_button = letsgo_wait.until(EC.element_to_be_clickable(
                (By.XPATH, "/html/body/div[8]/div/div/div/div[2]/div/div[4]/button/div")))
            letsgo_button.click()
        except TimeoutException:
            print("Lets go button not found. Pressing enter...")
            body = self.driver.find_element(By.TAG_NAME, 'body')
            body.send_keys(Keys.ENTER)

        sleep(1)


