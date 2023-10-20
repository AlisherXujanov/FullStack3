from django.test import TestCase

# Create your tests here.
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

PATH = "C:\\Users\\user\\Documents\\Alisher\\FullStack3\\chromedriver.exe"

HALF_SECOND = 0.5


class Fullstack(TestCase):

    def setUp(self):
        options = Options()
        options.add_argument('--headless')
        self.driver = webdriver.Chrome(service=Service(PATH), options=options)
        self.driver.maximize_window()
        # self.current_test = self.id().split(".")[-1]

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        print(f"Ending test for {self.driver}")

    def test_wikipedia(self):
        self.driver.get("http://127.0.0.1:8000/")
        print("Getting url...")
        h1 = self.driver.find_element(By.TAG_NAME, "h1")
        print('===============================================')
        print("Getting h1...")
        print("H1 text is: ", h1.text)
        print("H1 is: ", h1.text)
        print('===============================================')
