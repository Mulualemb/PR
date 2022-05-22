from random import randint
import Locators.register_locators
from selenium.webdriver.common.by import By




class Register_page:
    def __init__(self, driver):
        self.driver = driver
        self.register_page =  Locators.register_locators.RegisterLocators.register_page
        self.enter_pass = Locators.register_locators.RegisterLocators.enter_pass
        self.enter_confirm_pass = Locators.register_locators.RegisterLocators.enter_confirm_pass
        self.enter_email = Locators.register_locators.RegisterLocators.enter_email
        self.sign_up = Locators.register_locators.RegisterLocators.sign_up
        self.logout_button = Locators.register_locators.RegisterLocators.logout_button

    def click_register(self):
        self.driver.find_element(By.XPATH,self.register_page).click()

    def send_pass(self,a):
        self.driver.find_element(By.XPATH, self.enter_pass).send_keys(a)

    def send_confirm(self,a):
        self.driver.find_element(By.XPATH, self.enter_confirm_pass).send_keys(a)

    def send_email(self,a):
        self.driver.find_element(By.XPATH, self.enter_email).send_keys(a)

    def click_sign(self):
        self.driver.find_element(By.XPATH,self.sign_up).click()


    def rd(self):
        b = ""
        while len(b) < 9:
            a = randint(0, 9)
            b = b + str(a)
        return b
