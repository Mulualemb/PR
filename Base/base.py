import pytest
from selenium import webdriver
import jenkins


class Base:

    @pytest.fixture(autouse=True)
    def set_up(self):
        self.driver = webdriver.Chrome("../Chromedriver/chromedriver.exe")
        self.driver.implicitly_wait(10)
        self.driver.get("https://wondemagen-barbershop.herokuapp.com/")
        self.driver.maximize_window()
        yield self.driver
        if self.driver is not None:
            self.driver.close()
            self.driver.quit()