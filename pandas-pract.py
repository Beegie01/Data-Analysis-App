import pandas as pd, tkinter as tk, os
from tkinter import filedialog as fd

class CSVReader:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title('CSV FILE READER')
        sw, sh = int(self.root.winfo_screenwidth()*.5), int(self.root.winfo_screenheight()*.7)
        self.root.geometry('{w}x{h}'.format(w=sw, h=sh))
        self.root.resizable(0, 0)
        self.root.rowconfigure(0, weight=1), self.root.columnconfigure(0, weight=1)

        self.startpage()

        self.root.mainloop()

    def startpage(self):
        bg = 'green'
        frame = tk.Frame(self.root, bg=bg)
        frame.grid(sticky='nsew')
        frame.rowconfigure([0, 1, 2], weight=1), frame.columnconfigure(0, weight=1)

        lab = tk.Label(frame, text='CSV FILE READER\n\nBY BEEGIE\n\nJUNE 2021', font=('Calibri', 16, 'bold'), bg=bg, fg='white')
        lab.grid(sticky='nsew')

        frame.after(ms=2000, func=lambda: self.menupage(widg=frame))

    def menupage(self, widg):
        bg = 'purple'
        widg.grid_forget()
        self.root.geometry('170x50')#, self.root.rowconfigure(0, weight=1), self.root.columnconfigure([0, 1], weight=1)
        frame = tk.Frame(self.root, bg=bg)
        frame.grid(sticky='nsew')
        frame.rowconfigure(1, weight=1), frame.columnconfigure(0, weight=1)

        tk.Label(frame, text='Choose CSV File', bg=bg, fg='white').grid(sticky='ew')
        btn = tk.Button(frame, text='Open', bg='white', fg='green',
                  command=self.file_opener)
        btn.grid(row=0, column=1, sticky='ew', padx=4, pady=4)

        btn.bind('<Enter>', lambda event: btn.config(bg='yellow'))
        btn.bind('<Leave>', lambda event: btn.config(bg='white'))

    def file_opener(self):
        fp = fd.askopenfilename(initialdir=os.getcwd(), filetypes=[('CSV FILES', '*.csv')])
        print('Selected File:\t{}'.format(fp))
        self.csv_reader(fp)

    def csv_reader(self,  file_path, old_window=None):
        if old_window:
            old_window.destroy()

        bg = 'gold'
        fn = file_path.split('/')[-1]
        print(fn)
        win = tk.Toplevel()
        win.title(fn)
        sw, sh = int(self.root.winfo_screenwidth()*.5), int(self.root.winfo_screenheight()*.7)
        win.geometry('{w}x{h}'.format(w=sw, h=sh))
        win.resizable(0, 0)
        win.rowconfigure(0, weight=1), win.columnconfigure(0, weight=1)
        
        df = pd.read_csv(filepath_or_buffer=file_path)
        frame = tk.Frame(win, bg=bg)
        frame.grid(sticky='nsew')
        frame.rowconfigure(0, weight=1), frame.columnconfigure(0, weight=1)
        tk.Label(frame, text='FILE CONTENT:\n{}'.format(df), bg=bg, fg='black', font=('calibri', 12)).grid(sticky='nsew')
        info_btn = tk.Button(frame, text='Check Info', bg='blue', fg='white', command=lambda: self.disp_info(win, df, file_path))
        info_btn.grid(row=1, column=1)


        info_btn.bind('<Enter>', lambda event: info_btn.config(bg='pink'))
        info_btn.bind('<Leave>', lambda event: info_btn.config(bg='blue'))
        
    def disp_info(self, old_window, dataframe, file_path):
        old_window.destroy()
        bg = 'gold'
        fn = file_path.split('/')[-1]
        print(fn)
        win = tk.Toplevel()
        win.title(fn)
        sw, sh = int(self.root.winfo_screenwidth() * .5), int(self.root.winfo_screenheight() * .7)
        win.geometry('{w}x{h}'.format(w=sw, h=sh))
        win.resizable(0, 0)
        win.rowconfigure(0, weight=1), win.columnconfigure(0, weight=1)

        # dataframe.info()
        # print(type(dataframe.info()))
        frame = tk.Frame(win, bg=bg)
        frame.grid(sticky='nsew')
        frame.rowconfigure(0, weight=1), frame.columnconfigure(0, weight=1)

        tk.Label(frame,
                 text=f'CONTENT INFO:\nDataFrame Contains {dataframe.shape[0]} rows/indices and {dataframe.shape[1]} columns\n\n'
                      f'EXPLORATORY DATA ANALYSIS:\n{dataframe.describe().transpose()}',
                 bg=bg,
                 fg='black',
                 font=('calibri', 12)).grid(sticky='nsew')

        back_btn = tk.Button(frame, text='Back', bg='brown', fg='white', command=lambda: self.csv_reader(file_path, win))
        back_btn.grid(row=1)

        back_btn.bind('<Enter>', lambda event: back_btn.config(bg='pink'))
        back_btn.bind('<Leave>', lambda event: back_btn.config(bg='brown'))


if __name__ == '__main__':
    CSVReader()