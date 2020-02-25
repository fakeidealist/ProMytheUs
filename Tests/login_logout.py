from selenium import webdriver
from Keys.testdata import TestData
from Pages.page import LoginPage, TalentListPage
import unittest
import time

"""A class to perform logout test: first login, then logout"""


class Logout_Test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(executable_path='C:/geckodriver.exe')
        self.driver.implicitly_wait(7)
        self.driver.maximize_window()
        self.driver.get(TestData.BASE_URL)
        time.sleep(5)

    def test_login_logout(self):
        login = LoginPage(self.driver)
        logout = TalentListPage(self.driver)
        login.put_login_Info()
        login.click_signin()
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