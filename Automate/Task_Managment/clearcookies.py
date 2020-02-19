import unittest
from time import sleep
from selenium import webdriver
from datetime import date

Chrome_Driver = webdriver.Chrome(
    executable_path=r"C:\Users\badar.munir\Downloads\Automation\WebDrivers\chromedriver.exe")
url = "http://tms.drivrrsys.com/"
Chrome_Driver.get(url)







Chrome_Driver.find_element_by_id("emailInput").send_keys("obaid.farooq@nexuscorp-ltd.com")
Chrome_Driver.find_element_by_id("inputPassword").send_keys("system@123")
Chrome_Driver.find_element_by_xpath(
        "//*[@id='root']/section/div/div/div/div/div/div/div/div/div/div/form/button").click()

sleep(2)
cok = Chrome_Driver.get_cookies()
print(cok)
Chrome_Driver.delete_all_cookies()
cok = Chrome_Driver.get_cookies()
print(cok)
sleep(2)
Chrome_Driver.refresh()
