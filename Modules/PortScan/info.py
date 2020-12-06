# import libraries
import tkinter
from tkinter import PhotoImage


# window
class Window:

    # init
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.configure(background='#232328')
        self.window.resizable(width=False, height=False)
        self.window.title('PortScan info')
        self.info_txt = tkinter.Label(self.window, text='Comming soon...', bg='#232328', fg='#ffffff', font=16).pack()
        # quit_s = PhotoImage(file = 'Sprites/system/quit.png') self.quit_b = tkinter.Button(window, image = quit_s,
        # command = self.quit, bd = 0, relief = tkinter.FLAT, highlightthickness = 0, overrelief =
        # tkinter.FLAT).grid(row = 0, column = 1)
        self.window.mainloop()

    # quit
    # def quit(self):
    #    self.window.destroy()
