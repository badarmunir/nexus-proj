import os
import tkinter as tk
import uuid
from time import sleep

from selenium import webdriver

root = tk.Tk()
canvas1 = tk.Canvas(root, width=440, height=310, relief='raised')
root.resizable(0, 0)
canvas1.pack()

label1 = tk.Label(root, text='Check for external links')
label1.config(font=('helvetica', 14))
canvas1.create_window(220, 25, window=label1)

label2 = tk.Label(root, text='Enter blog url:')
label2.config(font=('helvetica', 10))
canvas1.create_window(220, 100, window=label2)

entry1 = tk.Entry(root, width="45")
canvas1.create_window(220, 140, window=entry1)


def GetInput():
    Url = entry1.get()
    if Url == '':
        pass
    else:
        entry1.delete(0, 'end')
        chrome = webdriver.Chrome(
            executable_path=r"chromedriver.exe")
        chrome.maximize_window()
        filename = str(uuid.uuid4())[:1]
        sleep(2)
        chrome.get(Url)
        match_Url = Url[12:29]
        sleep(2)
        all_elements = chrome.find_elements_by_tag_name("a")
        for i in all_elements:
            links = i.get_attribute("href")
            if Url in links or match_Url in links \
                    or "twitter.com" in links \
                    or "javascript" in links \
                    or "facebook.com" in links \
                    or "linkedin.com" in links \
                    or "mailto" in links:
                pass
                chrome.close()

            else:
                print(links)
                print(i.text)
                f = open(filename + ".txt", "a+")
                f.write("Base Url: " + Url + "\n")
                f.write("External link Url: " + links + "\n")
                f.write("External link text: " + i.text + "\n")
                f.close()
                filepath = os.path.abspath(filename)
                label5 = tk.Label(root, text='External links found', font=('helvetica', 10))
                canvas1.create_window(220, 210, window=label5)
                label6 = tk.Label(root, text='File At:' + filepath + ".txt", font=('helvetica', 10))
                canvas1.create_window(220, 250, window=label6)
                chrome.close()



button1 = tk.Button(text='Search', command=GetInput, bg='brown', fg='white',
                    font=('helvetica', 9, 'bold'))
canvas1.create_window(220, 180, window=button1)
root.mainloop()
