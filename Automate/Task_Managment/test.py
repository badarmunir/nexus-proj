
from selenium import webdriver
# from appium import webdriver
import unittest

from time import sleep


Chrome_Driver = webdriver.Chrome(
    executable_path=r"C:\Users\badar.munir\Downloads\Automation\WebDrivers\chromedriver.exe")
Chrome_Driver.get("https://www.google.com/")
Chrome_Driver.find_element_by_name("q").send_keys("daraz")
Chrome_Driver.find_element_by_xpath("//*[@id='tsf']/div[2]/div[1]/div[3]/center/input[1]").click()
Chrome_Driver.find_element_by_partial_link_text("Daraz.com: Online Marketplace in South Asia").click()
