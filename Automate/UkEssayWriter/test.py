from selenium import webdriver
from time import sleep
import xlrd

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
            sleep(2)
            Chrome.get(Url + "contact.php")
            sleep(2)
            Chrome.find_element_by_name("name").send_keys("Badar")
            Chrome.find_element_by_name("email").send_keys("Badar.munir@nexuscorp-ltd.com")
            Chrome.find_element_by_name("phone").send_keys("03402065923")
            Chrome.find_element_by_name("subject").send_keys("contact us")
            Chrome.find_element_by_name("message").send_keys("test message ")
            if Chrome.find_element_by_id("captcha").is_displayed():
                captcha_input = input("Enter Captcha")
                #Chrome.find_element_by_id("captcha").send_keys(captcha_input)
                Chrome.find_element_by_xpath("//*[@id='captcha']").send_keys(captcha_input)
            else:
                pass
        # Chrome.find_element_by_name("submit").click()


if __name__ == '__main__':
    obj = Test()
    obj.test_main()
    sleep(5)
