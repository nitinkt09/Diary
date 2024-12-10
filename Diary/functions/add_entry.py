import os
import tkinter as tk
from tkinter import *
from tkinter.messagebox import showerror, showinfo
import datetime



def done(text,date,entryBox, entriesDir,add):
        note = entryBox.get("1.0", tk.END)
        dayStr = date.strftime("%A")
        month = date.strftime("%B")
        yearStr = str(date.year)
        dateStr = str(date.strftime("%d"))
        yearInt = date.year
        dateInt = date.strftime("%d")
        monthStr = date.strftime("%m")
        
        Filename = dateStr + "-" + monthStr + "-" + yearStr + ".txt"
        header = "Date: " + dateStr + " " + month + " " + yearStr + "\nDay: " + dayStr + "\n\n"
        destination = entriesDir+Filename
        if os.path.isfile(destination):
            try:
                with open(destination, "at", encoding="utf-8") as file:
                    file.write("\n" + note)
                    entryBox.delete("1.0",tk.END)
                    showinfo("Success", "Previous entry edited")
            except:
                print("An exception occured while editing a previous file.")
                showerror("Error", "An exception occured while editing a previous file.")
            add.destroy()    
        else:
            try:
                with open(destination, "wt", encoding="utf-8") as file:
                    file.write(header + note)
                    entryBox.delete("1.0",tk.END)
                    showinfo("Success", "New entry saved")
            except:
                print("An exception occured while writing a new file.")
                showerror("Error", "An exception occured while writing a new file.")
            add.destroy()    
        
               