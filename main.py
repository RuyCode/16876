#import libraries
import tkinter
from tkinter import PhotoImage
from PIL import Image
from Modules.PortScan.Scan import Window as Window_ps
from Modules.DoS.Dos import Window as Window_dos
from Modules.DoS.info import Window as Window_dos_info
from Modules.PortScan.info import Window as Window_ps_info

#init window
mainwin = tkinter.Tk()
mainwin.title('MiniFramework v1.0')
mainwin.configure(background = '#232328')
mainwin.resizable(width = False, height = False)

#load sprites
quit_s = PhotoImage(file = 'Sprites/system/quit.png')
info_s = PhotoImage(file = 'Sprites/system/info.png')
ports_s = PhotoImage(file = 'Sprites/programs/portscan/portscan.png')
dos_s = PhotoImage(file = 'Sprites/programs/dos/dos.png')
infotxt_s = PhotoImage(file = 'Sprites/system/infotxt.png')

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
        inftxt = tkinter.Label(mainwin, image = infotxt_s, highlightthickness = 0, bd = 0)
        inftxt.grid(row = 1, column = 0, columnspan = 2, rowspan = 2, sticky = tkinter.NW)
        info_open = True

#create buttons
quit_b = tkinter.Button(mainwin, image = quit_s, command = quit, bd = 0, relief = tkinter.FLAT, highlightthickness = 0, overrelief = tkinter.FLAT).grid(row = 0, column = 3)
info_b = tkinter.Button(mainwin, image = info_s, command = infotext, bd = 0, relief = tkinter.FLAT, highlightthickness = 0, overrelief = tkinter.FLAT).grid(row = 0, column = 0)
ports_b = tkinter.Button(mainwin, image = ports_s, command = Window_ps, bd = 0, relief = tkinter.FLAT, highlightthickness = 0, overrelief = tkinter.FLAT).grid(row = 1, column = 1, padx = 8, pady = 16)
dos_b = tkinter.Button(mainwin, image = dos_s, command = Window_dos, bd = 0, relief = tkinter.FLAT, highlightthickness = 0, overrelief = tkinter.FLAT).grid(row = 2, column = 1, padx = 8, pady = 16)
info_dos_b = tkinter.Button(mainwin, image = info_s, command = Window_dos_info, bd = 0, relief = tkinter.FLAT, highlightthickness = 0, overrelief = tkinter.FLAT).grid(row = 2, column = 2)
info_ps_b = tkinter.Button(mainwin, image = info_s, command = Window_ps_info, bd = 0, relief = tkinter.FLAT, highlightthickness = 0, overrelief = tkinter.FLAT).grid(row = 1, column = 2)

#start window
mainwin.mainloop()
