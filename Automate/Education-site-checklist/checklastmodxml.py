
from bs4 import BeautifulSoup
import requests
from urllib.parse import urlparse
from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"C:\Users\badar.munir\Downloads\Automation\WebDrivers\chromedriver.exe")


def get_sitemap(url):
    get_url = requests.get(url)
