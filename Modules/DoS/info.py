#import libraries
import tkinter
from tkinter import PhotoImage

#window
class Window:

    #init
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.configure(background = '#232328')
        self.window.resizable(width = False, height = False)
        self.window.title('DoS attack info')
        self.infotxt = tkinter.Label(self.window, text = 'Comming soon...', bg = '#232328', fg = '#ffffff', font = 16).pack()
        #self.quit_s = PhotoImage(file = 'Sprites/system/quit.png')
        #self.quit_b = tkinter.Button(mainwin, image = self.quit_s, command = self.btn_click(), bd = 0, relief = tkinter.FLAT, highlightthickness = 0, overrelief = tkinter.FLAT).grid(row = 0, column = 1)
        self.window.mainloop()

    #quit
    #def btn_click(self):
    #    self.window.destroy()
