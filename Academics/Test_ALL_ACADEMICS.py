# import python packages

from selenium import webdriver
from time import sleep
import xlrd

# webdriver path
Chrome = webdriver.Chrome(executable_path=r"C:\Users\badar.munir\Downloads\Automation\WebDrivers\chromedriver.exe")

# file path with Urls
loc = r"C:\Users\badar.munir\Desktop\urls.xlsx"

# read excel file
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
sheet.cell_value(0, 0)

# maximize window
Chrome.maximize_window()


# main class test
class Test_ALL():
    def Order_now_1(self):
        # order now
        sleep(2)
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

    def Order_now_2(self):
        # order now
        sleep(2)
        Chrome.find_element_by_partial_link_text("Order").click()
        sleep(3)
        Chrome.find_element_by_id('paper_type').send_keys("Essay")
        Chrome.find_element_by_id('ref_style').send_keys("HARVARD")
        Chrome.find_element_by_id('edu_level').send_keys("Undergraduate")
        Chrome.find_element_by_id('subject').send_keys("English")
        Chrome.find_element_by_id('topic').send_keys("How To Write Essay")
        Chrome.find_element_by_id('instructions').send_keys("Essay should be summarized")
        Chrome.find_element_by_id('paper_standard').send_keys("2:1 Standard Guaranteed")
        Chrome.find_element_by_id("no_words").send_keys("500 words - 2 pages")
        el1 = Chrome.find_element_by_id("deadline")
        el1.click()
        sleep(2)
        Chrome.find_element_by_xpath("//*[@id='ui-datepicker-div']/table/tbody/tr[2]/td[1]/a").click()
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

    def Order_now_3(self):
        # order now
        sleep(2)
        Chrome.find_element_by_partial_link_text("Order").click()
        sleep(3)
        Chrome.find_element_by_id('paper_type').send_keys("Essay")
        Chrome.find_element_by_id('ref_style').send_keys("HARVARD")
        Chrome.find_element_by_id('edu_level').send_keys("Undergraduate")
        Chrome.find_element_by_id('subject').send_keys("English")
        Chrome.find_element_by_id('topic').send_keys("How To Write Essay")
        Chrome.find_element_by_id('instructions').send_keys("Essay should be summarized ")
        Chrome.find_element_by_id('paper_standard').send_keys("2:2 Standard Guaranteed")
        Chrome.find_element_by_id("no_words").send_keys("750 words - 3 pages")
        el1 = Chrome.find_element_by_id("deadline")
        el1.click()
        sleep(2)
        Chrome.find_element_by_xpath("//*[@id='ui-datepicker-div']/table/tbody/tr[2]/td[2]/a").click()
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

    def Contact_Us(self):
        # Contact Us
        sleep(2)
        Chrome.find_element_by_partial_link_text("Contact").click()

    def Sign_in(self, Url):
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
            sleep(2)

    def Forget_Password(self, Url):
        try:
            Chrome.get(Url + "clientarea/")
            Chrome.find_element_by_xpath("/html/body/section/div/div/div[2]/form/div[2]/label[2]/a").click()
            Chrome.find_element_by_xpath("/html/body/div[2]/div/div[2]/form/div/input[1]").send_keys(
                "amir.younus@nexuscorp-ltd.com")
            Chrome.find_element_by_xpath("/html/body/div[2]/div/div[2]/form/div/input[2]").click()
            Chrome.get(Url)
            sleep(2)
        except:
            sleep(2)

    def Sign_Up(self, Url):
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
            sleep(2)

    def main_function(self):
        # read excell
        wb = xlrd.open_workbook(loc)
        sheet = wb.sheet_by_index(0)
        sheet.cell_value(0, 0)
        for i in range(sheet.nrows):
            Url = sheet.cell_value(i + 1, 0)
            Chrome.get(Url)
            # check different type of order by
            self.Order_now_1()
            #self.Order_now_2()
            #self.Order_now_3()
            Chrome.get(Url)
            self.Contact_Us()
            self.Sign_in(Url)
            self.Forget_Password()
            self.Sign_Up()


if __name__ == '__main__':
    obj = Test_ALL()
    obj.main_function()
