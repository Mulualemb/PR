from Base.base import *
from Pages.register_page import *
from selenium.webdriver.support import expected_conditions as EC
from  selenium.webdriver.support.ui import WebDriverWait
from time import *


@pytest.mark.usefixtures('set_up')
class Test_register(Base):
    def test_successful_register(self):
        driver = self.driver
        register = Register_page(driver)
        register.click_register()
        register.send_pass("123123")
        register.send_confirm("123123")
        register.send_email(f"{register.rd()}@luo.uk")
        register.click_sign()
        value = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.XPATH,Locators.register_locators.RegisterLocators.logout_button))
        ).get_attribute("innerText")
        assert value == "log out"




    def test_failed_register_diff_passwords(self):
        driver = self.driver
        register = Register_page(driver)
        register.click_register()
        register.send_pass("123457")
        register.send_confirm("687456")
        register.send_email(f"{register.rd()}@ioi.ck")
        register.click_sign()
        value = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.XPATH,Locators.register_locators.RegisterLocators.sign_up))
        ).get_attribute("disabled")
        assert value == "true"

    def test_failed_register_null_fields(self):
        driver = self.driver
        register = Register_page(driver)
        register.click_register()
        register.send_pass("")
        register.send_confirm("")
        register.send_email("")
        register.click_sign()
        value = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.XPATH,Locators.register_locators.RegisterLocators.sign_up))
        ).get_attribute("disabled")
        assert value == "true"




    def test_failed_registration_null_confirm_password(self):
        driver = self.driver
        register = Register_page(driver)
        register.click_register()
        register.send_pass("123457")
        register.send_confirm("")
        register.send_email(f"{register.rd()}@ohy.ck")
        register.click_sign()
        value = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.XPATH,Locators.register_locators.RegisterLocators.sign_up))
        ).get_attribute("disabled")
        assert value == "true"



# simple test
    def test_failed_registration_null_password(self):
        driver = self.driver
        register = Register_page(driver)
        register.click_register()
        register.send_pass("")
        register.send_confirm(11223344)
        register.send_email(f"{register.rd()}@iuy.ck")
        register.click_sign()
        value = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.XPATH,Locators.register_locators.RegisterLocators.sign_up))
        ).get_attribute("disabled")
        assert value == "true"




    def test_failed_registration_null_pass_null_confirm(self):
        driver = self.driver
        register = Register_page(driver)
        register.click_register()
        register.send_pass("")
        register.send_confirm("")
        register.send_email(f"{register.rd()}@iuy.ck")
        register.click_sign()
        value = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.XPATH,Locators.register_locators.RegisterLocators.sign_up))
        ).get_attribute("disabled")
        assert value == "true"




    def test_failed_registration_invalid_email(self):
        driver = self.driver
        register = Register_page(driver)
        register.click_register()
        register.send_pass("112233")
        register.send_confirm("112233")
        register.send_email(f"{register.rd()}iuy.ck")
        register.click_sign()
        sleep(2)
        value = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.XPATH,Locators.register_locators.RegisterLocators.enter_email))
        ).get_attribute("validationMessage")
        assert value != ""



