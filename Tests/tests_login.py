import Locators.login_locators
from Base.base import *
from Pages.login_page import *
from selenium.webdriver.support import expected_conditions as EC
from  selenium.webdriver.support.ui import WebDriverWait


@pytest.mark.usefixtures('set_up')
class Test_login(Base):
    def test_successful_login(self):
        driver = self.driver
        login = Login_page(driver)
        login.click_login()
        login.enter_mail("el01@ma.co")
        login.enter_pass("112233")
        login.click_sign_in()
        value = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.XPATH,Locators.login_locators.LoginLocators.logout_button))
        ).get_attribute("innerText")
        assert value == "log out"




    def test_failed_login_wrong_pass(self):
        driver = self.driver
        login = Login_page(driver)
        login.click_login()
        login.enter_mail("el01@ma.co")
        login.enter_pass("22347jy")
        login.click_sign_in()
        value = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.XPATH, Locators.login_locators.LoginLocators.h4txt))
        ).get_attribute("innerText")
        assert value == "incorrect Password/Email"




    def test_failed_login_unregisterd_valid_mail(self):
        driver = self.driver
        login = Login_page(driver)
        login.click_login()
        login.enter_mail("einl@mail.com")
        login.enter_pass("11223344")
        login.click_sign_in()
        value = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.XPATH,Locators.login_locators.LoginLocators.h4txt))
        ).get_attribute("innerText")
        assert value == "incorrect Password/Email"




    def test_failed_login_ivalid_mail(self):
        driver = self.driver
        login = Login_page(driver)
        login.click_login()
        login.enter_mail("el01ma.corg")
        login.enter_pass("1122334455")
        login.click_sign_in()
        value = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.XPATH, Locators.login_locators.LoginLocators.login_enter_mail))
        ).get_attribute("validationMessage")
        assert value != ""




    def test_failed_login_null_pass_null_mail(self):
        driver = self.driver
        login = Login_page(driver)
        login.click_login()
        login.enter_mail("")
        login.enter_pass("")
        login.click_sign_in()
        value = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.XPATH, Locators.login_locators.LoginLocators.sign_in_button))
        ).get_attribute("disabled")
        assert value == "true"




    def test_failed_login_null_pass_valid_mail(self):
        driver = self.driver
        login = Login_page(driver)
        login.click_login()
        login.enter_mail("el01@ma.co")
        login.enter_pass("")
        login.click_sign_in()
        value = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.XPATH, Locators.login_locators.LoginLocators.sign_in_button))
        ).get_attribute("disabled")
        assert value == "true"