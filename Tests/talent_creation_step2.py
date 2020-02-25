from selenium import webdriver
from Keys.testdata import TestData
from Pages.page import LoginPage, TalentCreationPage_Step2
import unittest
import time

"""A class to perform talent creation in personal info session"""


class Create_Talent_Step2(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(executable_path='C:/geckodriver.exe')
        self.driver.implicitly_wait(7)
        self.driver.maximize_window()
        self.driver.get(TestData.BASE_URL)
        time.sleep(5)

    def test_select_talent(self):  # A method to select talent in category.
        #  Will remove login steps after main file works
        login = LoginPage(self.driver)
        step2 = TalentCreationPage_Step2(self.driver)

        login.put_login_Info()
        login.click_signin()

        time.sleep(2)

        time.sleep(2)

        time.sleep(2)

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        print("Logout test completed")


if __name__ == '__main__':
    unittest.main()