from selenium import webdriver
from time import sleep

Url = "https://www.lawessayshelp.co.uk/"

Chrome = webdriver.Chrome(executable_path=r"C:\Users\badar.munir\Downloads\Automation\WebDrivers\chromedriver.exe")
Chrome.maximize_window()
check_number = "0203-034-8530"
check_Disclimer = "British Essay Writers offers quality academic writing assistance through its experienced personnel. However, students, under no given circumstances, can submit our assistance as their original"
title = "Essay Writers UK, Essay Writing Service UK, Essay Help Online"

# main Class Test
class Test():
    # Open website Url
    def OpenUrl(self):
        Chrome.get(Url)
        sleep(2)

    # click on xmax Banner
    def click_on_xmax(self):
        Chrome.find_element_by_xpath("/html/body/div[12]/div[1]/button/span[1]").click()
        sleep(5)

    # Sign In
    def SignIn(self):
        Chrome.get(Url + "clientarea/")
        sleep(2)
        Chrome.find_element_by_xpath("/html/body/section/div/div/div[2]/form/div[1]/input").send_keys(
            "amir.younus@nexuscorp-ltd.com")
        Chrome.find_element_by_xpath("/html/body/section/div/div/div[2]/form/div[2]/input").send_keys(
            "system@123")
        Chrome.find_element_by_xpath("/html/body/section/div/div/div[2]/form/div[3]/div/input").click()

    # Forget Password
    def Forget_Password(self):
        sleep(2)
        Chrome.get(Url + "clientarea/")
        Chrome.find_element_by_xpath("/html/body/section/div/div/div[2]/form/div[2]/label[2]/a").click()
        Chrome.find_element_by_xpath("/html/body/div[2]/div/div[2]/form/div/input[1]").send_keys(
            "amir.younus@nexuscorp-ltd.com")
        Chrome.find_element_by_xpath("/html/body/div[2]/div/div[2]/form/div/input[2]").click()
        Chrome.get(Url)

    # Contact Us
    def contact_us(self):
        Chrome.get(Url)
        Chrome.find_element_by_partial_link_text("Contact").click()
        sleep(5)
        Chrome.find_element_by_xpath(
            "/html/body/div[4]/div/div/div/div/div[3]/div/div[2]/form/div/div[1]/div[1]/input").send_keys("Empty")
        Chrome.find_element_by_xpath(
            "/html/body/div[4]/div/div/div/div/div[3]/div/div[2]/form/div/div[4]/button[2]").click()
        sleep(3)
        Chrome.get("https://www.britishessaywriters.co.uk/contact-us.php")
        Chrome.find_element_by_xpath(
            "/html/body/div[4]/div/div/div/div/div[3]/div/div[2]/form/div/div[1]/div[1]/input").send_keys("--test--")
        Chrome.find_element_by_xpath(
            "/html/body/div[4]/div/div/div/div/div[3]/div/div[2]/form/div/div[2]/div[1]/input").send_keys("03402065923")
        Chrome.find_element_by_xpath(
            "/html/body/div[4]/div/div/div/div/div[3]/div/div[2]/form/div/div[1]/div[2]/input").send_keys(
            'badar.munir@nexuscorp-ltd.com')
        Chrome.find_element_by_xpath(
            "/html/body/div[4]/div/div/div/div/div[3]/div/div[2]/form/div/div[2]/div[2]/input").send_keys("Contact me ")
        Chrome.find_element_by_xpath(
            "/html/body/div[4]/div/div/div/div/div[3]/div/div[2]/form/div/div[3]/div/div/textarea").send_keys(
            "Need urgent help")
        # Chrome.find_element_by_xpath("/html/body/div[4]/div/div/div/div/div[3]/div/div[2]/form/div/div[4]/button[1]").click()

    # Sign-Up
    def Sign_Up(self):
        Chrome.get(Url)
        sleep(3)
        Chrome.find_element_by_xpath("//*[@id='signupform']/div/div/div[1]/div/input").send_keys("badar")
        sleep(2)
        Chrome.find_element_by_xpath("//*[@id='signupform']/div/div/div[2]/div/input").send_keys(
            "badar.munir@nexuscorporation-ltd.com")
        sleep(2)
        Chrome.find_element_by_xpath("//*[@id='signupform']/div/div/div[3]/div/input").send_keys("03402065923")
        # Chrome.find_element_by_xpath("//*[@id='signupform']/div/div/div[4]/div/input").click()

    # Order-Now
    def Order_now(self):
        Chrome.get(Url + "order-now.php")
        sleep(3)
        Chrome.find_element_by_id('paper_type').send_keys("Essay")
        Chrome.find_element_by_id('ref_style').send_keys("HARVARD")
        Chrome.find_element_by_id('edu_level').send_keys("Undergraduate")
        Chrome.find_element_by_id('subject').send_keys("English")
        Chrome.find_element_by_id('topic').send_keys("How To Write Essay")
        Chrome.find_element_by_id('instructions').send_keys("Essay should be summarized ")
        Chrome.find_element_by_id('paper_standard').send_keys("First Class Standard Guaranteed")
        Chrome.find_element_by_id("no_words").send_keys("250 words - 1 page")
        Chrome.find_element_by_id("deadline").send_keys("02/01/2020")
        Chrome.find_element_by_id('name').send_keys("badar")
        Chrome.find_element_by_id('email').send_keys("badar.munir@nexuscorporation-ltd.com")
        Chrome.find_element_by_id('country').send_keys("American Samoa")
        Chrome.find_element_by_id("phone1").send_keys("034000000")
        # Captcha Input
        user = input("Enter Captcha")
        Chrome.find_element_by_id("code").send_keys(user)
        # Discount Coupon
        Chrome.find_element_by_id("coupon").send_keys("12345")
        # Chrome.find_element_by_id("coupon_btn").click()
        Chrome.find_element_by_xpath("//*[@id='OrderForm']/div[4]/div/div/div/div[1]/label/input").click()
        # Chrome.find_element_by_xpath("//*[@id='OrderForm']/div[4]/div/div/span/input").click()
        Chrome.back()


if __name__ == '__main__':
    obj = Test()
    # obj.OpenUrl()
    # obj.SignIn()
    # obj.Forget_Password()
    # obj.Sign_Up()
    # obj.Order_now()
    #obj.contact_us()
    # Chrome.quit()
