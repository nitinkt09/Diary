import os
import tkinter as tk
from tkinter.messagebox import showerror, showinfo,askyesno



def delete_file (date,entriesDir,delete):
    filename= entriesDir+date+'.txt'
    if os.path.isfile(filename):
        response = askyesno(
            'Delete',
            'Are you sure you want to delete?'
        )
        if response:
            print(filename+" exists")
            os.remove(filename)
            showinfo("Success", "Entry removed") 	
        delete.destroy()
    else:
        print(filename+" doesn't exists")
        showerror(message=filename+" doesn't exists")
        delete.destroy()