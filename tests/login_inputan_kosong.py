import unittest
import requests
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class Login_Inputan_Kosong(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.browser = webdriver.Edge()
    
    def test_1_login_page(self):           
        self.browser.get('http://localhost/BadCRUD-main/login.php')
        self.browser.find_element(By.ID, "inputUsername").send_keys("admin")
        self.browser.find_element(By.ID, "inputPassword").send_keys(Keys.CONTROL + "nimda")
        self.browser.find_element(By.ID, "inputPassword").send_keys(Keys.DELETE)
        self.browser.find_element(By.TAG_NAME, 'button').click()
        
    @classmethod
    def tearDownClass(cls):
        time.sleep(2)

if __name__ == '__main__':
    unittest.main(verbosity=2, warnings='ignore')

