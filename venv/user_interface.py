from tkinter import *

from tkinter import messagebox


window = Tk()
window.title("IP-Infosystem 1.0")
window.geometry('400x200')

#def clicked():
#    messagebox.showinfo('IP not resolvable', 'The information you entered is not an IP address, or the IP cannot be accessed')

lbl1 = Label(text='Enter IP-Address')
lbl1.grid(column=0, row=1, padx=5, pady=5)

ipinp = Entry(text='Enter IP-Address')
ipinp.grid(column=1, row=1, padx=5, pady=5)

btn1 = Button(text='Search IP')
btn1.grid(column=3,row=1, padx=5, pady=5)

btn2 = Button(text='Use own IP')
btn2.grid(column=4,row=1, padx=5, pady=5)

window.mainloop()