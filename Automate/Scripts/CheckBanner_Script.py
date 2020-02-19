from selenium import webdriver
from time import sleep
import xlrd

# Use this script to check banner in URL

Chrome = webdriver.Chrome(executable_path=r"C:\Users\badar.munir\Downloads\Automation\WebDrivers\chromedriver.exe")
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
            sleep(4)
            try:
                # check if banner is present
                # if Chrome.find_element_by_id("signupdiscount-header-form").is_displayed():

                # check Sign-up now banner
                if Chrome.find_element_by_class_name("tclass").is_displayed():
                    print(Url)
                # check if banner is not present
            except:
                # print(Url)
                continue


if __name__ == '__main__':
    obj = Test()
    obj.test_main()
