from selenium import webdriver
from Locators.locators import LoginPageLocators, SignupPageLocators,\
    TalentListPageLocators, CreateTalentPageLocators_Step1, CreateTalentPageLocators_Step2
from Keys.testdata import LoginPageData, SignupPageData, TalentCreationPageData_Step2

"""using page object pattern"""


class BasePage(object):  # Base class to initiate the base page that will be called from all pages
    def __init__(self, driver):
        self.driver = driver


class LoginPage(BasePage):
    def put_login_Info(self):  # Method to put login email and password
        enter_email = self.driver.find_element(*LoginPageLocators.put_Email)
        enter_email.send_keys(LoginPageData.login_email)
        enter_password = self.driver.find_element(*LoginPageLocators.put_Password)
        enter_password.send_keys(LoginPageData.login_password)

    def click_signin(self):  # Method to click login button
        click_signin = self.driver.find_element(*LoginPageLocators.login_Button)
        click_signin.click()


class SignupPage(BasePage):
    def click_signup(self):  # Method to click signup button
        click_signup = self.driver.find_element(*LoginPageLocators.signup_Button)
        click_signup.click()

    def put_sign_up_Info(self):  # Method to put all info for account signup
        enter_firstname = self.driver.find_element(*SignupPageLocators.put_FirstName)
        enter_firstname.send_keys(SignupPageData.signup_firstname)
        enter_lastname = self.driver.find_element(*SignupPageLocators.put_LastName)
        enter_lastname.send_keys(SignupPageData.signup_lastname)
        enter_email = self.driver.find_element(*SignupPageLocators.put_Email)
        enter_email.send_keys(SignupPageData.signup_email)
        enter_phonenumber = self.driver.find_element(*SignupPageLocators.put_PhoneNumber)
        enter_phonenumber.send_keys(SignupPageData.signup_phonenumber)
        enter_address = self.driver.find_element(*SignupPageLocators.put_Address)
        enter_address.send_keys(SignupPageData.signup_address)
        enter_city = self.driver.find_element(*SignupPageLocators.put_City)
        enter_city.send_keys(SignupPageData.signup_city)
        enter_state = self.driver.find_element(*SignupPageLocators.put_State)
        enter_state.send_keys(SignupPageData.signup_state)
        enter_zip = self.driver.find_element(*SignupPageLocators.put_ZipCode)
        enter_zip.send_keys(SignupPageData.signup_zip)
        enter_password = self.driver.find_element(*SignupPageLocators.put_Password)
        enter_password.send_keys(SignupPageData.signup_password)
        enter_repassword = self.driver.find_element(*SignupPageLocators.put_RePassword)
        enter_repassword.send_keys(SignupPageData.signup_repassword)

    def click_agree_signup(self):
        click_agree = self.driver.find_element(*SignupPageLocators.checkbox_Agree)
        click_agree.click()

    # def click_create(self):
    #     click_create = self.driver.find_element(*SignupPageLocators.click_Create)
    #     click_create.click()


class TalentHomePage(BasePage):
    def click_user_icon(self):
        click_user = self.driver.find_element(*TalentListPageLocators.user_Icon)
        click_user.click()

    def click_logout(self):
        click_logout = self.driver.find_element(*TalentListPageLocators.user_Logout)
        click_logout.click()

    def click_new_talent(self):
        click_new = self.driver.find_element(*TalentListPageLocators.talent_New)
        click_new.click()


class TalentCreationPage_Step1(BasePage):
    def click_talent_category(self):
        category_dropdown = self.driver.find_element(*CreateTalentPageLocators_Step1.catagory_dropdown)
        category_dropdown.click()
        select_talent = self.driver.find_element(*CreateTalentPageLocators_Step1.dance_talent)
        select_talent.click()

    def click_next(self):
        click_next = self.driver.find_element(*CreateTalentPageLocators_Step1.next_button)
        click_next.click()


class TalentCreationPage_Step2(BasePage):
    def put_name(self):
        enter_firstname = self.driver.find_element(*CreateTalentPageLocators_Step2.put_FirstName)
        enter_firstname.send_keys(TalentCreationPageData_Step2.put_firstname)
        enter_middlename = self.driver.find_element(*CreateTalentPageLocators_Step2.put_MiddleName)
        enter_middlename.send_keys(TalentCreationPageData_Step2.put_middlename)
        enter_lastname = self.driver.find_element(*CreateTalentPageLocators_Step2.put_LastName)
        enter_lastname.send_keys(TalentCreationPageData_Step2.put_lastname)

    def select_profile_picture(self):
        pass

    def select_gender(self):
        select_gender = self.driver.find_element(*CreateTalentPageLocators_Step2.click_Other)
        select_gender.click()

    def put_date_place_birth(self):
        put_birthdate = self.driver.find_element(*CreateTalentPageLocators_Step2.enter_birthdate)
        put_birthdate.send_keys(TalentCreationPageData_Step2.put_birthdate)
        put_birthplace = self.driver.find_element(*CreateTalentPageLocators_Step2.enter_birthplace)
        put_birthplace.send_keys(TalentCreationPageData_Step2.put_birthplace)

    def put_location(self):
        pass

    def put_contact_details(self):
        pass

    def put_social_media_Info(self):
        pass

    def put_height_weight(self):
        pass

class TalentCreationPage_Step3(BasePage):
    pass