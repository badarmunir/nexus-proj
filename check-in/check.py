# libraries
import os
from tkinter import *

# variables
path = "credentials.txt"
if not os.path.isfile(path):
    login = Tk()
    checkin = Tk()
    checkin.iconify()
else:
    checkin = Tk()

username = StringVar()
password = StringVar()


# register user
def register_user():
    # get username and password
    username_info = username.get()
    password_info = password.get()
    if username_info and password_info != None:
        # Open file in write mode
        pth = "credentials.txt"
        write_file = open(pth, "w+")
        # write username and password information into file
        write_file.write(username_info + "\n")
        write_file.write(password_info)
        write_file.close()
        read_file = open(pth)
        lines = read_file.readlines()
        user = lines[0]
        pswd = lines[1]
        print(user)
        print(pswd)
        read_file.close()
        login.destroy()
        Display_Checkin_screen()


# display login screen
def Display_Login_Screen():
    login.overrideredirect(1)  # will remove the top badge of window
    login.resizable(False, False)
    window_height = 350
    window_width = 650
    screen_width = login.winfo_screenwidth()
    screen_height = login.winfo_screenheight()
    login.configure(background='#27282C')
    x_cordinate = int((screen_width / 2) - (window_width / 2))
    y_cordinate = int((screen_height / 2) - (window_height / 2))
    canvas = Canvas(login, width=970, height=5, borderwidth=2, highlightthickness=0,
                    bg="orange")
    Logintext = Label(login, text="LOGIN",
                      foreground="#FFFFFF",
                      background="#27282C",
                      font="-weight bold"
                      )

    username_entry = Entry(login, textvariable=username,
                           foreground="#FFFFFF",
                           background="#27282C",
                           font="50",
                           borderwidth=3,
                           width="25",
                           )

    password_entry = Entry(login, textvariable=password, show='*',
                           foreground="#FFFFFF",
                           background="#27282C",
                           font="50",
                           borderwidth=3,
                           width="25",
                           )

    btn = Button(login, text="LOGIN", width=25, command=register_user,
                 foreground="#FFFFFF",
                 background="#F1A93A",
                 font="20",
                 )

    Company = Label(login, text="www.nexuscorp-ltd.com",
                    foreground="#FFFFFF",
                    background="#27282C",
                    font="-weight bold",
                    )
    canvas.pack()
    Logintext.pack()
    Logintext.place(x=300, y=100)
    username_entry.pack()
    username_entry.place(x=210, y=140)
    password_entry.pack()
    password_entry.place(x=210, y=180)
    btn.pack()
    btn.place(x=210, y=220)
    Company.pack()
    Company.place(x=230, y=320)
    login.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))


# read write file
def read_file_write_file():
    path = "credentials.txt"
    if os.path.isfile(path):
        file = open(path)
        lines = file.readlines()
        username = lines[0]
        pswd = lines[1]
        print(username)
        print(pswd)
    else:
        Display_Login_Screen()
        login.mainloop()


# display check-in screen
def Display_Checkin_screen():
    checkin.deiconify()
    checkin.overrideredirect(1)  # will remove the top badge of window
    checkin.resizable(False, False)
    window_height = 400
    window_width = 880
    screen_width = checkin.winfo_screenwidth()
    screen_height = checkin.winfo_screenheight()
    checkin.configure(background='#27282C')
    x_cordinate = int((screen_width / 2) - (window_width / 2))
    y_cordinate = int((screen_height / 2) - (window_height / 2))
    canvas = Canvas(checkin, width=970, height=5, borderwidth=2, highlightthickness=0,
                    bg="orange")

    checkin.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
    Text1 = Label(checkin, text="CHECK IN MISSING",
                  foreground="#F1A93A",
                  background="#27282C",
                  font='50',
                  pady="60")

    Text2 = Label(checkin, text="Check-in not found,Please try again",
                  foreground="#FFFFFF",
                  background="#27282C",
                  font='50',
                  pady="35"
                  )

    Text3 = Label(checkin, text="Please Check-in to continue...", foreground="#FFFFFF",
                  background="#27282C", font='50', pady="35")

    button = Button(checkin, text="Verify",
                    foreground="#000000",
                    background="#F1A93A",
                    height=1,
                    width=35,
                    font="20",
                    pady="5")

    Text4 = Label(checkin, text="1.0.0.0(07-01-2020)",
                  foreground="white",
                  background="#27282C",
                  font='15',
                  pady="10",

                  )

    Text5 = Label(checkin, text="www.nexuscorp-ltd.com",
                  foreground="white",
                  background="#27282C",
                  font='15',
                  pady="10",
                  )
    canvas.pack()
    Text1.pack()
    # Text2.pack()
    Text3.pack()
    button.pack()
    Text4.pack(side=LEFT, expand=YES, fill=BOTH)
    Text5.pack(side=RIGHT, expand=YES, fill=BOTH)


# main function
def main():
    read_file_write_file()
    Display_Checkin_screen()
    checkin.mainloop()


if __name__ == '__main__':
    main()
