from datetime import datetime
import tkinter as tk
from tkinter import Toplevel,Button
from tkcalendar import DateEntry,Calendar
from functions.add_entry import done
from functions.open_entry import file
from functions.delete_entry import delete_file




def calendar_view(window,entry_add,entriesDir):
        top = Toplevel(window)
        top.geometry('550x450')
        today=datetime.now()
        top.title('Calender')
        y=today.year
        m=today.month
        d=today.day
        cal = Calendar(top,font=("Comic Sans MS", 15, "bold"), selectmode='day', borderwidth=2,
                       background='black',foreground='white', year=y, month=m, day=d,maxdate=today)
        cal.pack(fill="both", expand=True)
        def print_sel():
            date_time=cal.selection_get()
            done(entry_add.get("1.0", tk.END),date_time,entry_add,entriesDir,window)
            top.destroy()
        Button(top,width=90,text="Ok",font=("Comic Sans MS", 15, "bold"),bg='#000000',fg='#FFFFFF',command=print_sel).pack()

def dateentry_view(window,entriesDir,txtarea):
    top = Toplevel(window)
    top.title("Date Entry")
    top.configure(bg='#000000')
    cal = DateEntry(top, width=12, background='black',foreground='white', borderwidth=2,font=("Comic Sans MS", 15),)
    cal.pack(padx=10, pady=10)
    def print_sel():
        c=cal.get_date()
        date=c.strftime('%d-%m-%Y')
        print(date)
        file (date,entriesDir,txtarea)
        top.destroy()    
    Button(top,width=20,text="Ok",font=("Comic Sans MS", 15, "bold"),bg='#000000',fg='#FFFFFF',command=print_sel).pack()       


def dateentry_delete(window,entriesDir):
        top = Toplevel(window)
        top.title("Date Entry")
        top.configure(bg='#000000')
        cal = DateEntry(top, width=12, background='black',foreground='white', borderwidth=2,font=("Comic Sans MS", 15),)
        cal.pack(padx=10, pady=10)
        def print_sel():
            c=cal.get_date()
            date=c.strftime('%d-%m-%Y')
            print(date)
            delete_file (date,entriesDir,window)
            top.destroy()    
        Button(top,width=20,text="Ok",font=("Comic Sans MS", 15, "bold"),bg='#000000',fg='#FFFFFF',command=print_sel).pack() 