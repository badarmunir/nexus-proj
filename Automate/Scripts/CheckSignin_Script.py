from selenium import webdriver
from time import sleep
import xlrd

# Use this script to check Signin in URL

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
                # check urls with sign-in area

                Chrome.get(Url + "clientarea/")
                Chrome.find_element_by_xpath("/html/body/section/div/div/div[2]/form/div[1]/input").send_keys(
                    "amir.younus@nexuscorp-ltd.com")
                Chrome.find_element_by_xpath("/html/body/section/div/div/div[2]/form/div[2]/input").send_keys(
                    "system@123")
                Chrome.find_element_by_xpath("/html/body/section/div/div/div[2]/form/div[3]/div/input").click()
                sleep(2)
            except:
                print(Url)
                continue
            sleep(2)


if __name__ == '__main__':
    obj = Test()
    obj.test_main()
