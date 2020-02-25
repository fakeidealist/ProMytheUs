from selenium import webdriver
from Keys.testdata import TestData
from Pages.page import LoginPage
import unittest
import time

"""A class to perform login test only"""


class Login_Test(unittest.TestCase):  # Class for login test

    def setUp(self):
        self.driver = webdriver.Firefox(executable_path='C:/geckodriver.exe')
        self.driver.implicitly_wait(7)
        self.driver.maximize_window()
        self.driver.get(TestData.BASE_URL)
        time.sleep(5)

    def test_login(self):
        login = LoginPage(self.driver)
        login.put_login_Info()
        login.click_signin()

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        print("Login test completed")


if __name__ == '__main__':
    unittest.main()