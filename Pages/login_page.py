from selenium.webdriver.common.by import By
import Locators.login_locators



class Login_page:
    def __init__(self,driver):
        self.driver = driver
        self.login_button = Locators.login_locators.LoginLocators.login_button
        self.login_enter_mail = Locators.login_locators.LoginLocators.login_enter_mail
        self.login_enter_pass = Locators.login_locators.LoginLocators.login_enter_pass
        self.sign_in_button = Locators.login_locators.LoginLocators.sign_in_button
        self.logout_button = Locators.login_locators.LoginLocators.logout_button


    def click_login(self):
        self.driver.find_element(By.XPATH,self.login_button).click()

    def enter_mail(self,a):
        self.driver.find_element(By.XPATH,self.login_enter_mail).send_keys(a)

    def enter_pass(self, a):
        self.driver.find_element(By.XPATH, self.login_enter_pass).send_keys(a)

    def click_sign_in(self):
        self.driver.find_element(By.XPATH, self.sign_in_button).click()


