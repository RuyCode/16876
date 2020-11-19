#import libraries
import tkinter
from tkinter import PhotoImage
from PIL import Image
from Modules.PortScan.PortScan import Window

#init window
mainwin = tkinter.Tk()
mainwin.title("MiniFramework v1.0")
mainwin.configure(background='#232328')
mainwin.geometry('384x256')
mainwin.resizable(width = False, height = False)

#load sprites
quit_s = PhotoImage(file="Sprites/System/quit.png")
info_s = PhotoImage(file="Sprites/System/info.png")
ports_s = PhotoImage(file="Sprites/programs/portscan.png")
infotxt_s = PhotoImage(file="Sprites/System/infotxt.png")

#info txt works with it :3
info_open = False

#create info
def infotext():
    global info_open
    global inftxt
    if info_open:
        inftxt.destroy()
        info_open = False
    else:
        inftxt = tkinter.Label(mainwin, image=infotxt_s, highlightthickness=0, bd = 0)
        inftxt.grid(row=1, column=0, columnspan = 2, rowspan = 2, sticky = tkinter.NW)
        info_open = True

#create buttons
quitb = tkinter.Button(mainwin, image=quit_s, command = quit, bd=0, relief=tkinter.FLAT, highlightthickness=0, overrelief=tkinter.FLAT).grid(row=0, column=2, padx = 96)
infob = tkinter.Button(mainwin, image=info_s, command = infotext, bd=0, relief=tkinter.FLAT, highlightthickness=0, overrelief=tkinter.FLAT).grid(row=0, column=0)
portsb = tkinter.Button(mainwin, image=ports_s, command = Window, bd=0, relief=tkinter.FLAT, highlightthickness=0, overrelief=tkinter.FLAT).grid(row=1, column=1, padx = 32, pady = 32)

#start window
mainwin.mainloop()
