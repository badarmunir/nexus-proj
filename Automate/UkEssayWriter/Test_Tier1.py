from selenium import webdriver
from time import sleep
import xlrd

Chrome = webdriver.Chrome(executable_path=r"C:\Users\badar.munir\Downloads\Automation\WebDrivers\chromedriver.exe")
loc = r"C:\Users\badar.munir\Desktop\urlsp.xlsx"

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
            # order now
            Chrome.find_element_by_partial_link_text("Order").click()
            sleep(3)
            Chrome.find_element_by_id('paper_type').send_keys("Essay")
            Chrome.find_element_by_id('ref_style').send_keys("HARVARD")
            Chrome.find_element_by_id('edu_level').send_keys("Undergraduate")
            Chrome.find_element_by_id('subject').send_keys("English")
            Chrome.find_element_by_id('topic').send_keys("How To Write Essay")
            Chrome.find_element_by_id('instructions').send_keys("Essay should be summarized ")
            Chrome.find_element_by_id('paper_standard').send_keys("First Class Standard Guaranteed")
            Chrome.find_element_by_id("no_words").send_keys("250 words - 1 page")
            el1 = Chrome.find_element_by_id("deadline")
            el1.click()
            sleep(2)
            Chrome.find_element_by_xpath("//*[@id='ui-datepicker-div']/table/tbody/tr[1]/td[7]/a").click()
            sleep(2)
            Chrome.find_element_by_id("name").send_keys("badar")
            Chrome.find_element_by_id("email").send_keys("badar.munir@nexuscorporation-ltd.com")
            Chrome.find_element_by_id("country").send_keys("Dominica")
            Chrome.find_element_by_id("phone1").send_keys("034000000")
            # Captcha Input
            user = input("Enter Captcha")
            Chrome.find_element_by_id("code").send_keys(user)
            # Discount Coupon
            Chrome.find_element_by_id("coupon").send_keys("12345")
            # Chrome.find_element_by_id("coupon_btn").click()
            Chrome.find_element_by_class_name("radio-button").click()
            # Chrome.find_element_by_xpath("//*[@id='OrderForm']/div[4]/div/div/span/input").click()
            Chrome.back()
            sleep(2)
            # Contact Us
            Chrome.get(Url)
            sleep(2)
            Chrome.find_element_by_partial_link_text("Contact").click()
            try:
                # sign-in
                Chrome.get(Url + "clientarea/")
                Chrome.find_element_by_xpath("/html/body/section/div/div/div[2]/form/div[1]/input").send_keys(
                    "amir.younus@nexuscorp-ltd.com")
                Chrome.find_element_by_xpath("/html/body/section/div/div/div[2]/form/div[2]/input").send_keys(
                    "system@123")
                Chrome.find_element_by_xpath("/html/body/section/div/div/div[2]/form/div[3]/div/input").click()
                sleep(2)
            except:
                continue
            sleep(2)
            # Forget_Password
            try:
                Chrome.get(Url + "clientarea/")
                Chrome.find_element_by_xpath("/html/body/section/div/div/div[2]/form/div[2]/label[2]/a").click()
                Chrome.find_element_by_xpath("/html/body/div[2]/div/div[2]/form/div/input[1]").send_keys(
                    "amir.younus@nexuscorp-ltd.com")
                Chrome.find_element_by_xpath("/html/body/div[2]/div/div[2]/form/div/input[2]").click()
                Chrome.get(Url)
                sleep(2)
            except:
                continue

            # Sign-Up
            try:
                Chrome.get(Url)
                sleep(3)
                Chrome.find_element_by_xpath("//*[@id='signupform']/div/div/div[1]/div/input").send_keys("badar")
                sleep(2)
                Chrome.find_element_by_xpath("//*[@id='signupform']/div/div/div[2]/div/input").send_keys(
                    "badar.munir@nexuscorporation-ltd.com")
                sleep(2)
                Chrome.find_element_by_xpath("//*[@id='signupform']/div/div/div[3]/div/input").send_keys("03402065923")
                # Chrome.find_element_by_xpath("//*[@id='signupform']/div/div/div[4]/div/input").click()
                sleep(2)
            except:
                continue






if __name__ == '__main__':
    obj = Test()
    obj.test_main()
