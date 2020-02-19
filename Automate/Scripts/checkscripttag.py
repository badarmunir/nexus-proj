from selenium import webdriver
from time import sleep
import xlrd

# Use this script to check Signin in URL
from selenium.webdriver.common.keys import Keys

Chrome = webdriver.Chrome(executable_path=r"C:\Users\badar.munir\Downloads\Automation\WebDrivers\chromedriver.exe")

# add all the urls

loc = r"C:\Users\badar.munir\Desktop\urls.xlsx"

wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
sheet.cell_value(0, 0)

Chrome.maximize_window()


class Test():

    # Open website Url from excel sheet
    def test_main(self):
        wb = xlrd.open_workbook(loc)
        sheet = wb.sheet_by_index(0)
        sheet.cell_value(0, 0)
        for i in range(sheet.nrows):
            Url = sheet.cell_value(i + 1, 0)
            Chrome.get(Url)
            try:
                Script_tag = Chrome.find_elements_by_tag_name("script")
                for i in Script_tag:
                    match_src = i.get_attribute("src")
                    if match_src == "https://www.googleadservices.com/pagead/conversion.js":
                        print(Url)
            except:
                print(Url)
                pass


if __name__ == '__main__':
    obj = Test()
    obj.test_main()
