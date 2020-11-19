#import libraryis
import socket
import tkinter
import os
import Modules.PortScan.Scan as s

class Window():
    def __init__(self):
        self.window = tkinter.Tk()
        self.path_ = 'Logs\log.txt'
        self.window.configure(background='#232328', width = 512, height = 768)
        self.window.resizable(width = False, height = False)
        self.window.title('PortChecker v0.1')
        self.host_label = tkinter.Label(self.window, text = 'Host:', bg='#232328', fg='#ffffff', font = 16).pack()
        self.host_entry = tkinter.Entry(self.window, fg='white', bg='#494949', width=30)
        self.host_entry.pack()
        self.port_start_label = tkinter.Label(self.window, text = 'Port_Start (minimum = 0):', bg='#232328', fg='#ffffff', font = 16).pack()
        self.port_start_entry = tkinter.Entry(self.window, fg='white', bg='#494949', width=30)
        self.port_start_entry.pack()
        self.port_end_label = tkinter.Label(self.window, text = 'Port_End (maximum = 65534):', bg='#232328', fg='#ffffff', font = 16).pack()
        self.port_end_entry = tkinter.Entry(self.window, fg='white', bg='#494949', width=30)
        self.port_end_entry.pack()
        self.path_label = tkinter.Label(self.window, text = 'Enter a path to  file:', bg='#232328', fg='#ffffff', font = 16).pack()
        self.path_entry = tkinter.Entry(self.window, fg='white', bg='#494949', width=30)
        self.path_entry.pack()
        self.access_data = tkinter.Button(self.window, text = 'access data', width = 10, height = 1, command = self.btn_click, font = 30, fg = '#ffffff', bg = '#232328').pack()
        self.window.mainloop()

    def btn_click(self):

        self.path_ = self.path_entry.get()
        self.host = self.host_entry.get()
        self.port_start = self.port_start_entry.get()
        self.port_end = self.port_end_entry.get()

        #check data
        if self.port_start.isdigit() and self.port_end.isdigit():
            self.port_start = int(self.port_start)
            self.port_end = int(self.port_end)
        else:
            self.port_start = 0
            self.port_end = 0
        if os.path.exists(self.path_) == False:
            if os.path.exists('Logs') == False:
                os.mkdir('Logs')
            self.path_ = 'Logs\log.txt'

        s.Scan(self.path_, self.port_start, self.port_end, self.host, self.window)
