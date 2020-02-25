"""Collection of locators in https://app.promytheus.net/"""

from selenium.webdriver.common.by import By


class LoginPageLocators(object):  # A class for login page locators.
    put_Email = (By.XPATH, "//input[@placeholder='Enter email']")
    put_Password = (By.XPATH, "//input[@placeholder='Password']")
    password_Reset = (By.XPATH, "//a[@class='text-muted']")
    login_Button = (By.XPATH, "//button[@id='login']")
    signup_Button = (By.XPATH, "//a[@class='btn btn-block btn-default']")


class SignupPageLocators(object):  # A class for signup page locators.
    put_FirstName = (By.XPATH, "//input[@id='signUpFirstName']")
    put_LastName = (By.XPATH, "//input[@id='signUpLastName']")
    put_Email = (By.XPATH, "//input[@id='signUpRegisterEmail']")
    put_PhoneNumber = (By.XPATH, "//input[@id='signUpPhone']")
    put_Address = (By.XPATH, "//input[@id='signUpAddress']")
    put_City = (By.XPATH, "//input[@id='signUpCity']")
    put_State = (By.XPATH, "//input[@id='signUpState']")
    put_ZipCode = (By.XPATH, "//input[@id='signUpZip']")
    put_Password = (By.XPATH, "//input[@id='signUpRegisterPassword']")
    put_RePassword = (By.XPATH, "//input[@id='signUpRegisterRePassword']")
    checkbox_Agree = (By.XPATH, "//div[@class='col-sm-12 text-center line-top p-v']//span[@class='fa fa-check']")
    click_Create = (By.XPATH, "//button[@id='createAccount']")


class TalentListPageLocators(object):  # A class for talent page locators.
    brand_Logo = (By.XPATH, "//div[@class='brand-logo']//img[@class='img-responsive']")
    user_Icon = (By.XPATH, "//em[@class='icon-user']")
    user_MyProfile = (By.XPATH, "//p[contains(text(),'My Profile')]")
    user_Logout = (By.XPATH, "//p[contains(text(),'Sign Out')]")
    row_dropdown = (By.XPATH,
                "//select[@class='form-control m-b ng-valid ng-not-empty ng-dirty ng-valid-parse ng-touched']")
    talent_New = (By.XPATH, "//a[@class='btn btn-primary mr']")
    talent_Enable = (By.XPATH, "//button[contains(text(),'Enable')]")
    talent_Disable = (By.XPATH, "//button[contains(text(),'Disable')]")
    talent_Archive = (By.XPATH, "//button[contains(text(),'Archive')]")
    select_All = (By.XPATH,
                  "//table[@class='table table-bordered table-hover table-head-text-center']//thead//tr//th//span[@class='fa fa-check']")
    select_First = (By.XPATH, "//tr[1]//td[1]//div[1]//label[1]//span[1]")
    select_Second = (By.XPATH, "//tr[2]//td[1]//div[1]//label[1]//span[1]")
    select_Third = (By.XPATH, "//tr[3]//td[1]//div[1]//label[1]//span[1]")
    select_Forth = (By.XPATH, "//tr[4]//td[1]//div[1]//label[1]//span[1]")
    select_Fifth = ((By.XPATH, "//tr[5]//td[1]//div[1]//label[1]//span[1]"))
    put_Search = (By.XPATH, "//input[@placeholder='Search']")
    click_Search = (By.XPATH, "//button[@class='btn btn-sm btn-default']")


class CreateTalentPageLocators_Step1(object):  # A class for talent page locators in catagory section.
    #  Create talent page step 1 locators.
    catagory_dropdown = (By.XPATH,
                         "//div[@class='col-lg-10']//div[@name='category']//span[@class='btn btn-default form-control ui-select-toggle']")
    dance_talent = (By.XPATH, "//span[contains(text(),'Dance (1.3)')]")
    next_button = (By.XPATH, "//div[@class='form-wizard-footer']//button[@class='btn btn-primary ng-binding'][contains(text(),'Next')]")


class CreateTalentPageLocators_Step2(object):
    # Create talent page step 2 locators.
    put_FirstName = (By.XPATH, "//input[@placeholder='Enter First name']")
    put_MiddleName = (By.XPATH, "//input[@placeholder='Enter Middle name']")
    put_LastName = (By.XPATH, "//input[@placeholder='Enter Last name']")
    insert_ProfilePicture = (By.XPATH,
                             "//button[@name='profilePicture']//span[@class='buttonText'][contains(text(),'Choose file')]")
    click_Male = (By.XPATH, "//label[contains(text(),'Male')]")
    click_Female = (By.XPATH, "//label[contains(text(),'Female')]")
    click_Other = (By.XPATH, "//label[contains(text(),'Other')]")
    click_calendar_icon = (By.XPATH, "//button[@class='btn btn-default']")
    click_calendar_year = (By.XPATH, "//span[contains(text(),'2018')]")
    click_calender_month = (By.XPATH, "//span[contains(text(),'January')]")
    click_calendar_date = (By.XPATH, "//span[@class='ng-binding'][contains(text(),'01')]")
    enter_birthdate = (By.XPATH, "//input[@placeholder='Enter Date of Birth']")
    enter_birthplace = (By.XPATH, "//input[@placeholder='Enter Place of Birth']")
    enter_country = (By.XPATH, "//div[@id='signUpCountry']//i[@class='caret pull-right']")
    enter_city = (By.XPATH, "//input[@placeholder='Enter city']")
    enter_state = (By.XPATH, "//input[@placeholder='Enter state']")
    enter_zip = (By.XPATH, "//input[@placeholder='Enter postal code']")
    click_rural = (By.XPATH, "//label[contains(text(),'Rural')]")
    click_urban = (By.XPATH, "//label[contains(text(),'Urban')]")
    click_privileged = (By.XPATH, "//label[contains(text(),'Privileged')]")
    click_underprivileged = (By.XPATH, "//label[contains(text(),'Underprivileged')]")
    enter_contact_email = (By.XPATH, "//input[@placeholder='Enter Email']")
    enter_contact_phone = (By.XPATH, "//input[@placeholder='Enter Phone']")
    enter_height = (By.XPATH, "//input[@placeholder='Enter Height']")
    enter_weight = (By.XPATH, "//input[@placeholder='Enter Weight']")
    next_button = (By.XPATH,
                   "//div[@class='form-wizard-footer']//button[@class='btn btn-primary ng-binding'][contains(text(),'Next')]")
    previous_button = (By.XPATH, "//button[@class='btn btn-primary mr-sm']")


class CreateTalentPageLocators_Step3(object):
    pass


class CreateTalentPageLocators_Step4(object):
    pass