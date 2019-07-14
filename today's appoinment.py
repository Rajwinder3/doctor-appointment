from tkinter import *
from tkinter.ttk import Treeview
from tkinter import ttk
class main:
    def __init__(self):
        self.win=Tk()
        height=self.win.winfo_screenheight()
        width=self.win.winfo_screenwidth()
        x=(width-700)//2
        y=(height-700)//2
        self.win.geometry('700x700+{}+{}'.format(str(x),str(y)))
        self.win.resizable(width=False, height=False)
        
        self.frame=Frame(self.win, height=700, width=700,bg="#334d4d")
        self.frame.place(x=0,y=0)
        
        self.frame1=Frame(self.frame, height=700, width=3, bg="#669999")
        self.frame1.place(x=5,y=0)
        self.frame2=Frame(self.frame, height=500, width=3, bg="#a3c2c2")
        self.frame2.place(x=15,y=0)
        self.frame3=Frame(self.frame, height=700, width=3, bg="#00756e")
        self.frame3.place(x=20,y=0)
        self.frame3=Frame(self.frame, height=200, width=3, bg="#e0ebeb")
        self.frame3.place(x=25,y=0)

        self.table=Treeview(self.frame, column=("#0","#1","#2","#3","#4","#5","#6"))
        self.table=Treeview(self.frame, column=("#0","#1","#2","#3","#4","#5","#6","#7"))
        style=ttk.Style()
        style.theme_use("alt")
        ttk.Style().configure("Treeview.Heading" ,font=('',10,"bold"))
        

        self.table.column("#0", width=70)
        self.table.column("#1", width=90)
        self.table.column("#2", width=80)
        self.table.column("#3", width=80)
        self.table.column("#4", width=80)
        self.table.column("#5", width=80)
        self.table.column("#6", width=80)
                
        self.table.heading("#0",text="Sr.")
        self.table.heading("#1",text="Patient Name")
        self.table.heading("#2",text="Gender")
        self.table.heading("#3",text="Age")
        self.table.heading("#4",text="Timing")
        self.table.heading("#5",text="Description")
        self.table.heading("#6",text="History")
    
        self.table.place(x=60,y=50, width=560,)

        self.win.mainloop()

f=main()
