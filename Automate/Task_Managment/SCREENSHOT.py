import unittest
from time import sleep
from selenium import webdriver
from datetime import date

Chrome_Driver = webdriver.Chrome(
    executable_path=r"C:\Users\badar.munir\Downloads\Automation\WebDrivers\chromedriver.exe")
url = "http://tms.drivrrsys.com/"
Chrome_Driver.get(url)



Chrome_Driver.set_window_size(9000,2763)
Chrome_Driver.save_screenshot("login.png")



Chrome_Driver.find_element_by_id("emailInput").send_keys("obaid.farooq@nexuscorp-ltd.com")
Chrome_Driver.find_element_by_id("inputPassword").send_keys("system@123")
Chrome_Driver.find_element_by_xpath(
        "//*[@id='root']/section/div/div/div/div/div/div/div/div/div/div/form/button").click()
sleep(5)
Chrome_Driver.save_screenshot("dashboard.png")

