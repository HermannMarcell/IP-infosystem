import tkinter
import requests
import ipaddress
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

def info1_class():
    collected_data = get_location()
    info1 = collected_data['ip']
    return info1

def info2_class():
    collected_data = get_location()
    info2 = collected_data['IP-version']
    return info2

def info3_class():
    collected_data = get_location()
    info3 = collected_data['city']
    return info3

def info4_class():
    collected_data = get_location()
    info4 = collected_data['postal code']
    return info4

def info5_class():
    collected_data = get_location()
    info5 = collected_data['region']
    return info5

def info6_class():
    collected_data = get_location()
    info6 = collected_data['country']
    return info6

def info7_class():
    collected_data = get_location()
    info7 = collected_data['internet host']
    return info7


def get_location():
#   ip_address = get_ip()
    response = requests.get(f'https://ipapi.co/{getinput()}/json/').json()
    location_data = {
        "ip": response.get("ip"),
        "IP-version": response.get("version"),
        "city": response.get("city"),
        "postal code": response.get("postal"),
        "region": response.get("region"),
        "country": response.get("country_name"),
        "internet host": response.get("org")
    }
    return location_data

def getinput():
    ip_address = ipinp.get()
    return ip_address

def destroy():
    outp1.destroy()
    outp2.destroy()
    outp3.destroy()
    outp4.destroy()
    outp5.destroy()
    outp6.destroy()
    outp7.destroy()

def changebutton():
    if info2_class() == None:
        messagebox.showinfo('IP not resolvable',
                            'The information you entered is not an IP address, or the IP cannot be accessed')
    else:
        destroy()
        outp1 = Label(text=info1_class())
        outp1.grid(column=1, row=2, padx=5, pady=5, columnspan=3)
        outp2 = Label(text=info2_class())
        outp2.grid(column=1, row=3, padx=5, pady=5, columnspan=3)
        outp3 = Label(text=info3_class())
        outp3.grid(column=1, row=4, padx=5, pady=5, columnspan=3)
        outp4 = Label(text=info4_class())
        outp4.grid(column=1, row=5, padx=5, pady=5, columnspan=3)
        outp5 = Label(text=info5_class())
        outp5.grid(column=1, row=6, padx=5, pady=5, columnspan=3)
        outp6 = Label(text=info6_class())
        outp6.grid(column=1, row=7, padx=5, pady=5, columnspan=3)
        outp7 = Label(text=info7_class())
        outp7.grid(column=1, row=8, padx=5, pady=5, columnspan=3)

def own_ip_info():
    ip_address = requests.get('https://api64.ipify.org?format=json').json()
    response = requests.get(f'https://ipapi.co/{ip_address["ip"]}/json/').json()
    location_data = {
        "ip": response.get("ip"),
        "IP-version": response.get("version"),
        "city": response.get("city"),
        "postal code": response.get("postal"),
        "region": response.get("region"),
        "country": response.get("country_name"),
        "internet host": response.get("org")
    }
    return location_data

def dataflow():
    getinput()
    get_location()
    changebutton()

def dataflow2():
    own_ip_info()
    changebutton()

#def clicked():
#    messagebox.showinfo('IP not resolvable', 'The information you entered is not an IP address, or the IP cannot be accessed')

lbl1 = Label(text='Enter IP-Address')
lbl1.grid(column=0, row=1, padx=5, pady=15)

#ipinp = Entry(text='Enter IP-Address')
#ipinp.grid(column=1, row=1, padx=5, pady=15)

ipinp = Entry()
ipinp.grid(column=1, row=1, padx=5, pady=15)

btn1 = Button(text='Search IP', command=dataflow)
btn1.grid(column=2,row=1, padx=5, pady=15)

btn2 = Button(text='Use own IP', command=dataflow2)
btn2.grid(column=3,row=1, padx=5, pady=15)

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