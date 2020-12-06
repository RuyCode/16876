# import libraries
import tkinter
from tkinter import PhotoImage
from Modules.DoS.Dos import Window as Window_dos
from Modules.DoS.info import Window as Window_dos_info
from Modules.PortScan.Scan import Window as Window_ps
from Modules.PortScan.info import Window as Window_ps_info

# init window
main_win = tkinter.Tk()
main_win.title('MiniFramework v1.0')
main_win.configure(background='#232328')
main_win.resizable(width=False, height=False)

# load sprites
quit_s = PhotoImage(file='Sprites/system/quit.png')
info_s = PhotoImage(file='Sprites/system/info.png')
ports_s = PhotoImage(file='Sprites/programs/portscan/portscan.png')
dos_s = PhotoImage(file='Sprites/programs/dos/dos.png')
info_txt_s = PhotoImage(file='Sprites/system/infotxt.png')

# info txt works with it :3
info_open = False


# create info
def info_text():
    global info_open
    global inf_txt
    if info_open:
        inf_txt.destroy()
        info_open = False
    else:
        inf_txt = tkinter.Label(main_win, image=info_txt_s, highlightthickness=0, bd=0)
        inf_txt.grid(row=1, column=0, columnspan=2, rowspan=2, sticky=tkinter.NW)
        info_open = True


# create buttons
quit_b = tkinter.Button(main_win, image=quit_s, command=quit, bd=0, relief=tkinter.FLAT, highlightthickness=0,
                        overrelief=tkinter.FLAT).grid(row=0, column=3)
info_b = tkinter.Button(main_win, image=info_s, command=info_text, bd=0, relief=tkinter.FLAT, highlightthickness=0,
                        overrelief=tkinter.FLAT).grid(row=0, column=0)
ports_b = tkinter.Button(main_win, image=ports_s, command=Window_ps, bd=0, relief=tkinter.FLAT, highlightthickness=0,
                         overrelief=tkinter.FLAT).grid(row=1, column=1, padx=8, pady=16)
dos_b = tkinter.Button(main_win, image=dos_s, command=Window_dos, bd=0, relief=tkinter.FLAT, highlightthickness=0,
                       overrelief=tkinter.FLAT).grid(row=2, column=1, padx=8, pady=16)
info_dos_b = tkinter.Button(main_win, image=info_s, command=Window_dos_info, bd=0, relief=tkinter.FLAT,
                            highlightthickness=0, overrelief=tkinter.FLAT).grid(row=2, column=2)
info_ps_b = tkinter.Button(main_win, image=info_s, command=Window_ps_info, bd=0, relief=tkinter.FLAT,
                           highlightthickness=0, overrelief=tkinter.FLAT).grid(row=1, column=2)

# start window
main_win.mainloop()
