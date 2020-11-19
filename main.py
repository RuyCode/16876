#import libraries
import pygame
import tkinter
from tkinter import PhotoImage
from PIL import Image
from Modules.PortScan import Window

mainwin = tkinter.Tk()
mainwin.title("MiniFramework v1.0")
mainwin.configure(background='#232328')

quit_s = PhotoImage(file="Sprites/System/quit.png")
info_s = PhotoImage(file="Sprites/System/info.png")
ports_s = PhotoImage(file="Sprites/programs/portscan.png")
infotxt_s = PhotoImage(file="Sprites/System/infotxt.png")

def infotext():
    inftxt = tkinter.Label(mainwin, image=infotxt_s, highlightthickness=0, bd = 0).grid(row=1, column=0, columnspan = 2, rowspan = 2, sticky = tkinter.NW)

mainwin.geometry('384x256')
mainwin.resizable(width = False, height = False)
quitb = tkinter.Button(mainwin, image=quit_s, command = quit, bd=0, relief=tkinter.FLAT, highlightthickness=0, overrelief=tkinter.FLAT).grid(row=0, column=2, padx = 96)
infob = tkinter.Button(mainwin, image=info_s, command = infotext, bd=0, relief=tkinter.FLAT, highlightthickness=0, overrelief=tkinter.FLAT).grid(row=0, column=0)
portsb = tkinter.Button(mainwin, image=ports_s, command = Window, bd=0, relief=tkinter.FLAT, highlightthickness=0, overrelief=tkinter.FLAT).grid(row=1, column=1, padx = 32, pady = 32)

mainwin.mainloop()
