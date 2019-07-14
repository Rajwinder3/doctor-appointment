from tkinter import *
from tkinter.ttk import Treeview
from tkinter import ttk
import database_queries
import editappoint

class main:
    def __init__(self):
        self.tk=Tk()
        height=self.tk.winfo_screenheight()
        width=self.tk.winfo_screenwidth()
        
        y=(height-650)//2
        x=(width-650)//2
        self.tk.geometry('650x650+'+str(x)+'+'+str(y))
        
        self.tk.resizable(height=False,width=False)
        self.tk.title("manage patient")
        
        

        '''self.can=Canvas(self.tk,height="650",width="650")
        self.can.pack()
        self.img=PhotoImage(file="./image/img21.gif")
        self.can.create_image(0,0,image=self.img,anchor=NW)'''

        self.f=Frame(self.tk,height="100",width="700",bg="#070719")
        self.f.place(x=0,y=0)
        self.l=Label(self.f,text="Manage Appointment",fg="powder blue",font=('cooper black',30),bg="#070719")
        self.l.place(x=120,y=20)

        self.f1=Frame(self.tk,height="650",width="650",bg="#C2DFFF")
        self.f1.place(x=0,y=100)
        self.fr=Frame(self.f1,height="10",width="700",bg="#070719")
        self.fr.place(x=0,y=10)

        self.fr1=Frame(self.f1,height="70",width="700",bg="#070719")
        self.fr1.place(x=0,y=500)


        self.table=Treeview(self.f1,column=("#0","#1","#2","#3","#4","#5"))
        style=ttk.Style()
        style.theme_use("alt")
        ttk.Style().configure("Treeview.heading",font=('',15))
        
        self.table.heading("#0",text="Sno.")
        self.table.column("#0",width="40")
        self.table.heading("#1",text="P_name")
        self.table.column("#1",width="60")
        
        self.table.heading("#2",text="Timing")
        self.table.column("#2",width="70")
        self.table.heading("#3",text="Date")
        self.table.column("#3",width="70")
        self.table.heading("#4",text="Description")
        self.table.column("#4",width="70")
        self.table.heading("#5",text="Edit")
        self.table.column("#5",width="70")
        self.table.heading("#6",text="Delete")
        self.table.column("#6",width="70")
        self.table.place(x=80,y=140)

        
        r=database_queries.database()
        res=r.view_appoint()
        print(res)
        for i in res:
            
            self.table.insert('','end',text=i[0],value=(i[2],i[3],i[4],i[5],"Edit","Delete"))
            self.table.place(x=100,y=150)
            self.table.bind("<Double Button>",self.fun)
        
        self.tk.mainloop()
    def fun(self,f):
        #print(e)
        d1=self.table.focus()
        z=(self.table.item(d1))
        col1 = self.table.identify_column(f.x)
        if col1=="#5":
            y=editappoint.main(z["text"])
            print("edit")
            
        elif col1 == "#6":
            print("delete")

                      
