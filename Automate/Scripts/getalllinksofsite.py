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
            murl = Url[12:30]

            sleep(3)
            elem = Chrome.find_elements_by_class_name("viewBlogText")
            for ele in elem:
                a = Chrome.find_elements_by_tag_name("a")
                for i in a:
                    match = i.get_attribute("href")
                    if murl in match:
                        pass
                    else:
                        #print(match)
                        print(Url)





if __name__ == '__main__':
    obj = Test()
    obj.test_main()
