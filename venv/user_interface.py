from tkinter import *

from tkinter import messagebox


window = Tk()
window.title("IP-Infosystem 1.0")
window.geometry('400x285')
info1='test'
info2='test'
info3='test'
info4='test'
info5='test'
info6='test'
info7='test'
#def clicked():
#    messagebox.showinfo('IP not resolvable', 'The information you entered is not an IP address, or the IP cannot be accessed')

lbl1 = Label(text='Enter IP-Address')
lbl1.grid(column=0, row=1, padx=5, pady=15)

ipinp = Entry(text='Enter IP-Address')
ipinp.grid(column=1, row=1, padx=5, pady=15)

btn1 = Button(text='Search IP')
btn1.grid(column=3,row=1, padx=5, pady=15)

btn2 = Button(text='Use own IP')
btn2.grid(column=4,row=1, padx=5, pady=15)

lbl2 = Label(text='IP-Address:')
lbl2.grid(column=0, row=2, padx=5, pady=5)

outp1 = Label(text=info1)
outp1.grid(column=1, row=2, padx=5, pady=5)

lbl3 = Label(text='IP-version:')
lbl3.grid(column=0, row=3, padx=5, pady=5)

outp2 = Label(text=info2)
outp2.grid(column=1, row=3, padx=5, pady=5)

lbl4 = Label(text='city:')
lbl4.grid(column=0, row=4, padx=5, pady=5)

outp3 = Label(text=info3)
outp3.grid(column=1, row=4, padx=5, pady=5)

lbl5 = Label(text='postal code:')
lbl5.grid(column=0, row=5, padx=5, pady=5)

outp4 = Label(text=info4)
outp4.grid(column=1, row=5, padx=5, pady=5)

lbl6 = Label(text='region:')
lbl6.grid(column=0, row=6, padx=5, pady=5)

outp5 = Label(text=info5)
outp5.grid(column=1, row=6, padx=5, pady=5)

lbl7 = Label(text='country:')
lbl7.grid(column=0, row=7, padx=5, pady=5)

outp6 = Label(text=info6)
outp6.grid(column=1, row=7, padx=5, pady=5)

lbl8 = Label(text='host:')
lbl8.grid(column=0, row=8, padx=5, pady=5)

outp7 = Label(text=info7)
outp7.grid(column=1, row=8, padx=5, pady=5)

window.mainloop()