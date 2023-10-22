from selenium import webdriver
import undetected_chromedriver as uc
from fake_useragent import UserAgent

class seleniumGPT:
    def __init__(self):
        pass

    def start_driver(self, url):
        op = webdriver.ChromeOptions()
        # Your options setup
        op.add_argument(f"user-agent={UserAgent().random}")
        op.add_argument("user-data-dir=./")
        op.add_experimental_option("detach", True)
        op.add_experimental_option("excludeSwitches", ["enable-logging"])

        driver = uc.Chrome(chrome_options=op)
        driver.get(url)
        return driver
