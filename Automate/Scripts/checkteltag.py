import re
from time import sleep

import xlrd
from selenium import webdriver

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
        # Url = "https://www.lawessaywriters.co.uk/"
        Chrome.get(Url)
        sleep(4)

        try:
            phonenumber = Chrome.find_element_by_class_name("phoneNum")
            if phonenumber.is_displayed():
                available_number = phonenumber.text
                phoneNumRegex = re.compile(r'\d\d\d\d-\d\d\d-\d\d\d\d')
                mo = phoneNumRegex.search(available_number)
                print('Phone number found: ' + mo.group())
        except:
            try:
                phonenumber2 = Chrome.find_element_by_class_name("phoneNumber")
                if phonenumber2.is_displayed():
                    available_number = phonenumber2.text
                    phoneNumRegex = re.compile(r'\d\d\d\d-\d\d\d-\d\d\d\d')
                    mo = phoneNumRegex.search(available_number)
                    print('Phone number found: ' + mo.group())
            except:
                try:
                    phonenumber3 = Chrome.find_element_by_class_name("phonenum")
                    if phonenumber3.is_displayed():
                        available_number = phonenumber3.text
                        phoneNumRegex = re.compile(r'\d\d\d\d-\d\d\d-\d\d\d\d')
                        mo = phoneNumRegex.search(available_number)
                        print('Phone number found: ' + mo.group())
                except:
                    print(Url)
                    continue









if __name__ == '__main__':
    obj = Test()
    obj.test_main()
