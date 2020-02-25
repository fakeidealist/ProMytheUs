from selenium import webdriver
from Keys.testdata import TestData
from Pages.page import SignupPage
import unittest
import time

"""A class to do signup test"""


class Signup_Test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(executable_path='C:/geckodriver.exe')
        self.driver.implicitly_wait(7)
        self.driver.maximize_window()
        self.driver.get(TestData.BASE_URL)
        time.sleep(5)

    def test_signup(self):
        signup_page = SignupPage(self.driver)
        signup_page.click_signup()
        signup_page.put_sign_up_Info()
        signup_page.click_agree_signup()
        # signup_page.click_create()
        time.sleep(5)

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        print("Login test completed")


if __name__ == '__main__':
    unittest.main()