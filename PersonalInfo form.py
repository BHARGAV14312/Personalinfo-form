from tkinter import *
master = Tk()
Label(master, text='Personal information').grid(row=0)
Label(master, text='First Name').grid(row=1)
Label(master, text='Last Name').grid(row=2)
Label(master, text='Address').grid(row=3)
Label(master, text='Street').grid(row=4)
Label(master, text='City').grid(row=5)
Label(master, text='ZIPCode').grid(row=6)
e2 = Entry(master)
e3 = Entry(master)
e4 = Entry(master)
e5 = Entry(master)
e6 = Entry(master)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
e4.grid(row=4, column=1)
e5.grid(row=5, column=1)
e6.grid(row=6, column=1)
button1 = Button(master, text="submit")
button1.grid(row=7, column=2)
mainloop()