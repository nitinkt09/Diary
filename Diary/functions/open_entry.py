import os
import tkinter as tk
from tkinter.messagebox import showerror, showinfo


def file (date,entriesDir,txtarea):
    filename= entriesDir+date+'.txt'
    if os.path.isfile(filename):
        print(filename+" exists")
        showinfo(message=filename+' exists')

        with open(filename, 'rt') as tf:
            data = tf.read()
            txtarea.insert(tk.END, data)       

    else:
        print(filename+" doesn't exists")
        showerror(message=filename+" doesn't exists")
