from tkinter import *
from tkinter.ttk import Treeview
from tkinter import ttk
import database_queries
import editp
import hop


class main:
    def __init__(self):
        self.tk=Toplevel()
        height=self.tk.winfo_screenheight()
        width=self.tk.winfo_screenwidth()
        
        y=(height-650)//2
        x=(width-650)//2
        self.tk.geometry('650x650+'+str(x)+'+'+str(y))
        
        self.tk.resizable(height=False,width=False)
        self.tk.title("manage patient")

        self.f=Frame(self.tk,height="650",width="650",bg="#CEE3F6")
        self.f.place(x=0,y=0)

        self.f1=Frame(self.f,height="100",width="650",bg="#070719")
        self.f1.place(x=0,y=0)
        
        self.l=Label(self.f1,text="Manage Patient",font=('cooper black',35),fg="#CEE3F6",bg="#070719")
        self.l.place(x=150,y=20)

        self.fr=Frame(self.f,height="70",width="650",bg="#070719")
        self.fr.place(x=0,y=580)
        self.fr1=Frame(self.f,height="10",width="650",bg="#070719")
        self.fr1.place(x=0,y=560)

        
        self.table=Treeview(self.f,column=("#0","#1","#2","#3","#4","#5","#6","#7","#8","#9"))
        style=ttk.Style()
        style.theme_use("alt")
        ttk.Style().configure("Treeview.heading",font=('',30))
        self.table.heading("#0",text="sno")
        self.table.column("#0",width="30")
        self.table.heading("#1",text="Name")
        self.table.column("#1",width="60")
        self.table.heading("#2",text="Gender")
        self.table.column("#2",width="60")
        self.table.heading("#3",text="Age")
        self.table.column("#3",width="60")
        self.table.heading("#4",text="contact")
        self.table.column("#4",width="70")
        self.table.heading("#5",text="Address")
        self.table.column("#5",width="70")
        self.table.heading("#6",text="Email")
        self.table.column("#6",width="90")
        self.table.heading("#7",text="History")
        self.table.column("#7",width="70")

        self.table.heading("#8",text="Edit")
        self.table.column("#8",width="70")
        self.table.heading("#9",text="Delete")
        self.table.column("#9",width="70")
        self.table.place(x=0,y=200)

        

        s=database_queries.database()
        res=s.view_patient()
        print(res)
        for i in res:
            
            self.table.insert('','end',text=i[0],value=(i[1],i[2],i[3],i[4],i[5],i[6],"History","Edit","Delete"))
            self.table.bind("<Double Button>",self.trigger)
            self.table.place()

        self.tk.mainloop()
    def trigger(self,e):
        #print(e)
        d=self.table.focus()
        g=(self.table.item(d))
        col = self.table.identify_column(e.x)
        if col=="#8":
            y=editp.main(g["text"])
            print("edit")
            
        elif col == "#9":
            print("delete")
            f=del_appoint()

       
        


        

