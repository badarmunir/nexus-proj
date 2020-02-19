# from appium import webdriver
import unittest
from time import sleep
from selenium import webdriver
from datetime import date

Chrome_Driver = webdriver.Chrome(
    executable_path=r"C:\Users\badar.munir\Downloads\Automation\WebDrivers\chromedriver.exe")
url = "http://tms.drivrrsys.com/"
Chrome_Driver.get(url)
Chrome_Driver.maximize_window()


# project details section
title = "My project"
desc = "My project desc"
S_Date = "23/01/202"



class Test(unittest.TestCase):

    def test_sign_in(self):
        Chrome_Driver.find_element_by_id("emailInput").send_keys("obaid.farooq@nexuscorp-ltd.com")
        Chrome_Driver.find_element_by_id("inputPassword").send_keys("system@123")
        Chrome_Driver.find_element_by_xpath(
            "//*[@id='root']/section/div/div/div/div/div/div/div/div/div/div/form/button").click()

    def test_create_project(self):
        sleep(4)
        create_project = Chrome_Driver.find_element_by_class_name("create-btn")
        create_project.click()
        Send_Project_title = Chrome_Driver.find_element_by_name("title")
        Send_Project_title.send_keys(title)
        Send_Project_Desc = Chrome_Driver.find_element_by_name("description")
        Send_Project_Desc.send_keys(desc)
   



if __name__ == '__main__':
    obj = Test()
    obj.test_sign_in()
    obj.test_create_project()
