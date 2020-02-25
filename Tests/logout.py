from selenium import webdriver
from Keys.testdata import TestData
from Pages.page import LoginPage
from Pages.page import TalentListPage
import unittest
import time


"""A class to perform logout test: One method performs login; another performs logout"""
"""NOT YET WORKING"""


class Logout_Test(unittest.TestCase):  # A class do to login and logout, not yet working

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
        time.sleep(3)

    def test_logout(self):
        logout = TalentListPage(self.driver)
        logout.click_user_icon()
        time.sleep(2)
        logout.click_logout()
        time.sleep(3)

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        print("Logout test completed")


if __name__ == '__main__':
    unittest.main()