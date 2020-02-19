from time import sleep
import pytest
from selenium import webdriver


class Linkdin:
    def open_chrome(self):
        self.chrome_driver = webdriver.Chrome(
            executable_path=r"C:\Users\badar.munir\Downloads\Automation\WebDrivers\chromedriver.exe")

    def open_Url(self):
        self.chrome_driver.maximize_window()
        self.get_Url = self.chrome_driver.get("https://www.linkedin.com")

    def login(self):
        username = "badarmunir021@gmail.com"
        passs = "1995Worst"
        self.login = self.chrome_driver.find_element_by_class_name("nav__button-secondary")
        self.login.click()
        self.username = self.chrome_driver.find_element_by_id("username")
        self.pasword = self.chrome_driver.find_element_by_id("password")
        self.username.send_keys(username)
        self.pasword.send_keys(passs)
        self.signin = self.chrome_driver.find_element_by_xpath("//*[@id='app__container']/main/div/form/div[3]/button")
        self.signin.click()


class main:
    if __name__ == '__main__':
        obj = Linkdin()
        obj.open_chrome()
        obj.open_Url()
        obj.login()
