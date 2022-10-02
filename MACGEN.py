from getmac import get_mac_address as gma
from tkinter import *
import os



macadd = gma()
name = os.getlogin()
sentence = f"Hi, can you please add my device to the network?\n The device's MAC Address is {macadd}.\n Thank you"



window = Tk()
window.geometry('600x200')
window.option_add('*Font', '16')
creation = Label(window,text = f"Hi {name}! Your MAC address is ready! \nCopy and paste the following into the IT request:").pack()
f1 = Frame(window).pack()
e = Text(f1, width = 300, font=('Arial 18'), highlightthickness = 4, bd = 2)
e.insert(END, sentence)
e.pack()
window.mainloop()
