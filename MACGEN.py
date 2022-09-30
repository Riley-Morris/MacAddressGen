from getmac import get_mac_address as gma
import os
from docx import Document
from docx.shared import Pt
from tkinter import *


username = os.getlogin()
document = Document()
style = document.styles['Normal']
font = style.font
font.name = 'Nirmala UI Semilight'
font.size = Pt(14)
macadd = gma()
sentence = f"Hi, can you please add my device to the network? The device's MAC Address is {macadd}"
document.add_paragraph(sentence)
document.save(f'C:\\Users\\{username}\\Desktop\\MAC-ADDRESS.docx')


window = Tk()
creation = Label(window,text = 'File Created on Desktop! \n Look for the word doc MAC-ADDRESS.docx').pack()
window.mainloop()