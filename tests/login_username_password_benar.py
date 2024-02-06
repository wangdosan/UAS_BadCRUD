import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class Login_Username_Password_Benar(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.browser = webdriver.Edge()
    
    def test_1_login_page(self):           
        self.browser.get('http://localhost/BadCRUD-main/login.php')  
        self.browser.find_element(By.ID, "inputUsername").send_keys("admin")
        self.browser.find_element(By.ID, "inputPassword").send_keys("nimda666!")
        self.browser.find_element(By.TAG_NAME, 'button').click()

    def test_2_dashboard_page(self):           
        expected_result = "admin"
        
        actual_result = self.browser.find_element(By.XPATH, "//h2[contains(text(),'Halo,')]").text.split(', ')[1]
        self.assertIn(expected_result, actual_result)

        
    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2, warnings='ignore')

