import os
import tkinter as tk 
from tkinter import Button, Tk, Label, Frame, Text, Toplevel,Scrollbar
from functions.date.calender import calendar_view,dateentry_view,dateentry_delete
from functions.close import closeWindow 


# main window
window= Tk()
window.title('BotDiary')
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window.geometry(f'{screen_width}x{screen_height}+0+0')
window.iconbitmap('./icons/logo.ico')
window.configure(background='black')

entriesDir=os.getcwd()+'\\entries\\'

def add_entry():
    add= Toplevel(window)
    add.geometry("750x950")
    add.title("Add or Update")
    add.configure(background='black')
    def calendar():
        c=calendar_view(add,entry_add,entriesDir)

    frame_add = Frame(add,bg='#444444')
    Label(add, text="What's New? >.~ ", height=3,width=29,
        font=("Comic Sans MS", 20, "bold"),bg='#444444',fg='#FFFFFF',relief=tk.RAISED,
    ).pack(pady=30)
    v=Scrollbar(add, orient='vertical',)
    v.pack(side='right', fill='y')     
    entry_add = Text(add,height=15,width=50,bg='#444444',fg='#FFFFFF',
        font=("Comic Sans MS", 13),relief=tk.RAISED,yscrollcommand=v.set
    )
    v.config(command=entry_add.yview)   
    entry_add.pack()
    button_add = Button(add,height=2,width=10,borderwidth=2,text='SAVE',relief=tk.RAISED,
        font=("Comic Sans MS", 15, "bold"),bg='#444444',fg='#FFFFFF',command=calendar,
    )
    button_add.pack(side="top",padx=10,pady=20)      
    frame_add.pack(expand=True,padx=50,pady=100)     
    add.mainloop()   


def open_entry():
        open= Toplevel(window)
        open.geometry("750x950")
        open.title("Open")
        open.configure(bg='#000000')
        def dateentry():
            d=dateentry_view(open,entriesDir,txtarea)  
        frame_open = Frame(open,bg='#444444')
        Label(open, height=3,width=29,bg='#444444',fg='#FFFFFF',relief=tk.RAISED,
            text="What are you looking for? >_<'", font=("Comic Sans MS", 20, "bold"),
        ).pack(pady=30)
        button_add = Button(open,height=1,width=10,borderwidth=0,text='CHOOSE',relief=tk.RAISED,
                     font=("Comic Sans MS", 15, "bold"),bg='#444444',fg='#FFFFFF',command=dateentry,
        )
        button_add.pack(side="top",padx=5,pady=15) 
        v=Scrollbar(open, orient='vertical')
        v.pack(side='right', fill='y')
        txtarea = Text(open, width=60, height=34,relief=tk.RAISED,bg='#444444',fg='#FFFFFF',yscrollcommand=v.set,
        font=("Comic Sans MS", 10,'bold'))
        v.config(command=txtarea.yview)
        txtarea.pack(pady=20)      
        frame_open.pack(expand=True,padx=50,pady=100)    
        open.mainloop()               
                

def delete_entry():
        delete= Toplevel(window)
        delete.geometry("750x250")
        delete.title("Delete")
        delete.configure(bg='#000000')
        def dateentry_view():
            d=dateentry_delete(delete,entriesDir)
     
        frame_delete = Frame(delete,bg='#444444')
        Label( delete, height=3,width=29,bg='#444444',fg='#FFFFFF',relief=tk.RAISED,
           text="Which File do you want to delete? ", font=("Comic Sans MS", 20, "bold"),
            ).pack(pady=30)
        button_add = Button(delete,height=1,width=10,borderwidth=0,text='CHOOSE',relief=tk.RAISED,
                     font=("Comic Sans MS", 15, "bold"),bg='#444444',fg='#FFFFFF',command=dateentry_view,
        )
        button_add.pack(side="top",padx=5,pady=15) 
        frame_delete.pack(expand=True,padx=50,pady=100)    
        delete.mainloop()    
            

def close():
    print('close')
    d=closeWindow(window)

#body
frame = Frame(window,bg='#000000')

label = Label(
    text="Welcome Back >.< ",
    height=3,
    width=window.winfo_screenwidth(),
    font=("Comic Sans MS", 20, "bold"),
    bg='#444444',
    fg='#FFFFFF',
    relief=tk.RAISED,
).pack()

button = Button(
    frame,
    height=3,
    width=18,
    borderwidth=2,
    text='Add Or Update \nAn Entry',
    font=("Comic Sans MS", 15, "bold"),
    bg='#444444',
    fg='#FFFFFF',
    relief=tk.RAISED,
    command=add_entry,
).pack(
    side="top",
    padx=50,
    pady=10
)
button1 = Button(
    frame,
    height=3,
    width=18,
    borderwidth=2,
    text='Open An Entry',
    font=("Comic Sans MS", 15, "bold"),
    bg='#444444',
    fg='#FFFFFF',
    relief=tk.RAISED,
    command=open_entry,
).pack(
    side="top",
    padx=50,
    pady=10
)
button2 = Button(
    frame,
    height=3,
    width=18,
    borderwidth=2,
    text='Delete An Entry',
    font=("Comic Sans MS", 15, "bold"),
    bg='#444444',
    fg='#FFFFFF',
    relief=tk.RAISED,
    command=delete_entry,
).pack(
    side="top",
    padx=50,
    pady=10
)
button3 = Button(
    frame,
    height=2,
    width=18,
    borderwidth=2,
    text='Exit',
    font=("Comic Sans MS", 15, "bold"),
    bg='#444444',
    fg='#FFFFFF',
    relief=tk.RAISED,
    command=close,
).pack(
    side="bottom",
    padx=20,
    pady=10
)



frame.pack( expand=True,padx=50,pady=100)
window.mainloop()