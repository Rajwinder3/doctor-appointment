from tkinter import *
from tkinter.ttk import Treeview
from tkinter import ttk
import database_queries
import edit_receptionist
class window:
    def __init__(self):
        
        self.win=Tk()
        height=self.win.winfo_screenheight()
        width=self.win.winfo_screenwidth()
        x=(width-700)//2
        y=(height-700)//2
        self.win.geometry('700x700+{}+{}'.format(str(x),str(y)))
        self.win.resizable(width=False, height=False)
        
        self.frame=Frame(self.win, height=700, width=700,bg="#a3c2c2")
        self.frame.place(x=0,y=0)

        self.frame1=Frame(self.frame, bg="#e0ebeb", height=700, width=2)
        self.frame1.place(x=30,y=0)
        self.frame1=Frame(self.frame, bg="#75a3a3", height=700, width=4)
        self.frame1.place(x=20,y=0)
        self.frame1=Frame(self.frame, bg="#476b6b", height=700, width=6)
        self.frame1.place(x=10,y=0)

        self.frame1=Frame(self.frame, bg="#e0ebeb", height=2, width=700)
        self.frame1.place(x=0,y=30)
        self.frame1=Frame(self.frame, bg="#75a3a3", height=4, width=700)
        self.frame1.place(x=0,y=20)
        self.frame1=Frame(self.frame, bg="#476b6b", height=6, width=700)
        self.frame1.place(x=0,y=10)
        
        self.table=Treeview(self.frame, column=("#0","#1","#2","#3","#4","#5","#6","#7"))
        style=ttk.Style()
        style.theme_use("alt")
        ttk.Style().configure("Treeview.Heading" ,font=('',14,"bold"))
        
        self.table.column("#0", width=80)
        self.table.column("#1", width=80)
        self.table.column("#2", width=80)
        self.table.column("#3", width=80)
        self.table.column("#4", width=80)
        self.table.column("#5", width=80)
        self.table.column("#6", width=80)
        self.table.column("#7", width=80)
        
        self.table.heading("#0",text="Sr.")
        self.table.heading("#1",text="Name")
        self.table.heading("#2",text="Gender")
        self.table.heading("#3",text="Email")
        self.table.heading("#4",text="Contact")
        self.table.heading("#5",text="Address")
        self.table.heading("#6",text="Edit")
        self.table.heading("#7",text="Delete")

        x = database_queries.database()
        res = x.view_receptionist()
        #print(res)
        for i in res:
            self.table.insert('','end',text=i[0],value=(i[1],i[2],i[3],i[5],i[6],"edit","delete"))

        self.table.bind("<Double Button-1>",self.trigger) 
        self.table.place(x=40,y=50, width=640)
        
        self.win.mainloop()
    def trigger(self,e):
        row=self.table.focus()
        t=(self.table.item(row))
        col=self.table.identify_column(e.x)
        if col=="#6":
             y=edit_receptionist.window(t["text"])
             
             print("edit")
        elif(col=="#7"):
             o=database_queries.database()
             o.delete(t["text"])


