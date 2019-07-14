from tkinter import *
from tkcalendar import DateEntry, Calendar
import database_queries

class main:
    def __init__(self,n_):
        print(n_)
        self.n=n_
        ob=database_queries.database()
        re=ob.get_appoint_byn(n_)
        print(re)
        self.tk=Toplevel()
        
        self.frame=Frame(self.tk,height=700,width=700)
        self.frame.place(x=0,y=0)
        
        height=self.tk.winfo_screenheight()
        width=self.tk.winfo_screenwidth()
        
        y=(height-700)//2
        x=(width-700)//2
        self.tk.geometry('700x700+'+str(x)+'+'+str(y))
        
        self.tk.resizable(height=False,width=False)

        self.can=Canvas(self.frame,height="700",width="700")
        self.can.pack()
        self.img=PhotoImage(file="./images/img2.gif")
        self.can.create_image(0,0,image=self.img,anchor=NW)

        self.can.create_text(360,100,text="Edit appointment ",fill="powder blue",font=('Cooper Black',35))


        self.pn=StringVar(self.tk)
        self.pn.set(re[2])
        self.can.create_text(175,220,text="Patient Name",fill="sandybrown",font=('Cooper Black',25))
        self.e1=Entry(self.frame,font=('Cooper Black',18),borderwidth="2",textvariable=self.pn)
        self.e1.place(x=310,y=210)


        self.t=StringVar(self.tk)
        self.t.set(re[3])
        self.can.create_text(175,280,text="Timing",fill="sandybrown",font=('Cooper Black',25))
        self.e2=Entry(self.frame,font=('Cooper Black',18),borderwidth="2",textvariable=self.t)
        self.e2.place(x=310,y=260)


        self.date=StringVar(self.tk)
        self.date.set(re[4])
        self.can.create_text(175,330,text="Date",fill="sandybrown",font=('Cooper Black',25))
        

        self.dob = DateEntry(self.can,font=('cooper balck',12), bg='darkblue',fg='white', borderwidth="2",textvariable=self.date)
        self.dob.place(x=310,y=310)
        self.dob.config(width=30)

        self.des=StringVar(self.tk)
        self.des.set(re[5])
        self.can.create_text(175,380,text="Description",fill="sandybrown",font=('Cooper Black',25))
        self.e4=Entry(self.frame,font=('Cooper Black',18),borderwidth="2",textvariable=self.des)
        self.e4.place(x=310,y=360)
        
        
        self.btn=Button(self.frame,text="Update",fg="powder blue",bg="black",font=('Cooper Black',22),command=self.update)
        self.btn.place(x=310,y=450)

        self.tk.mainloop()
    
    def update(self):
        data=[self.e1.get(),self.e2.get(),self.dob.get(),self.des.get(),self.n]
        
        t=database_queries.database()
        t.update_appoint(data)
   
    

