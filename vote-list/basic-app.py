import tkinter as tk

f =open("votinglist.txt","a")
f.write("FirstName  FatherName  Cnic                   Votingid            Phonenumber\n")
f.close()
def show_entry_fields():
    #print("First Name: %s\nFather Name: %s\nCnic: %s\nVoting id: %s\nPhone number: %s\n" % (e1.get(), e2.get(), e3.get(), e4.get(), e5.get()))
    f =open("votinglist.txt","a")

    f.write(e1.get()+"      ")
    f.write(e2.get()+"       ")
    f.write(e3.get()+"         ")
    f.write(e4.get()+"           ")
    f.write(e5.get()+"\n")
    f.close()
master = tk.Tk()
tk.Label(master, 
         text="Name").grid(row=0)
tk.Label(master, 
         text="Father Name").grid(row=1)
tk.Label(master,
         text="Cnic").grid(row=2)
tk.Label(master,
         text="Voting id").grid(row=3)
tk.Label(master,
         text="Phone number").grid(row=4)


e1 = tk.Entry(master)
e2 = tk.Entry(master)
e3 = tk.Entry(master)
e4 = tk.Entry(master)
e5 = tk.Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
e4.grid(row=3, column=1)
e5.grid(row=4, column=1)

tk.Button(master, 
          text='Quit', 
          command=master.quit).grid(row=6,
                                    column=0,
                                    sticky=tk.W, 
                                    pady=4)
tk.Button(master, 
          text='submit', command=show_entry_fields).grid(row=6,
                                                       column=1,
                                                       sticky=tk.W, 
                                                       pady=4)
tk.mainloop()