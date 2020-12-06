# import libraries
import tkinter
import Modules.DoS.Dos_attack as dos_attack


# to run window, get data and start process
class Window:

    # init
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.configure(background='#232328', width=512, height=768)
        self.window.resizable(width=False, height=False)
        self.window.title('DDoS attack v0.1')
        self.host_label = tkinter.Label(self.window, text='Host:', bg='#232328', fg='#ffffff', font=16).pack()
        self.host_entry = tkinter.Entry(self.window, fg='white', bg='#494949', width=30)
        self.host_entry.pack()
        self.port_start_label = tkinter.Label(self.window, text='Port_Start (minimum = 0):', bg='#232328', fg='#ffffff',
                                              font=16).pack()
        self.port_start_entry = tkinter.Entry(self.window, fg='white', bg='#494949', width=30)
        self.port_start_entry.pack()
        self.port_end_label = tkinter.Label(self.window, text='Port_End (maximum = 65534):', bg='#232328', fg='#ffffff',
                                            font=16).pack()
        self.port_end_entry = tkinter.Entry(self.window, fg='white', bg='#494949', width=30)
        self.port_end_entry.pack()
        self.rounds_label = tkinter.Label(self.window, text='Enter number of "attacks":', bg='#232328', fg='#ffffff',
                                          font=16).pack()
        self.rounds_entry = tkinter.Entry(self.window, fg='white', bg='#494949', width=30)
        self.rounds_entry.pack()
        self.access_data = tkinter.Button(self.window, text='access data', width=10, height=1, command=self.btn_click,
                                          font=30, fg='#ffffff', bg='#232328').pack()
        self.window.mainloop()

    # button click
    def btn_click(self):

        # get data
        self.rounds = self.rounds_entry.get()
        self.host = self.host_entry.get()
        self.port_start = self.port_start_entry.get()
        self.port_end = self.port_end_entry.get()

        # check data
        if self.port_start.isdigit() and self.port_end.isdigit() and self.rounds.isdigit():
            self.port_start = int(self.port_start)
            self.port_end = int(self.port_end)
            self.rounds = int(self.rounds)
        else:
            self.port_start = 0
            self.port_end = 0
            self.rounds = 0

        # start scan
        dos_attack.dos_attack(self.rounds, self.port_start, self.port_end, self.host, self.window)
