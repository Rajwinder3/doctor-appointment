from tkinter import *
import database_queries
from tkcalendar import DateEntry, Calendar
class main:
    def __init__(self):
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

        self.can.create_text(360,100,text="Add appointment ",fill="#FF9933",font=('Cooper Black',35))
        
        self.can.create_text(175,220,text="Patient Name",fill="#99ccff",font=('Cooper Black',25))
        self.e1=Entry(self.frame,font=('Cooper Black',18),borderwidth="2")
        self.e1.place(x=310,y=210)
        
        self.can.create_text(175,280,text="Timing",fill="#99ccff",font=('Cooper Black',25))
        self.e2=Entry(self.frame,font=('Cooper Black',18),borderwidth="2")
        self.e2.place(x=310,y=260)
        
        self.can.create_text(175,330,text="Date",fill="#99ccff",font=('Cooper Black',25))
        '''self.e3=Entry(self.frame,font=('Cooper Black',18),borderwidth="2")
        self.e3.place(x=310,y=310)'''

        self.dob = DateEntry(self.can,font=('cooper balck',12), bg='darkblue',fg='white', borderwidth=2)
        self.dob.place(x=310,y=310)
        self.dob.config(width=30)

        
        
        self.can.create_text(175,380,text="Description",fill="#99ccff",font=('Cooper Black',25))
        self.e4=Entry(self.frame,font=('Cooper Black',18),borderwidth="2")
        self.e4.place(x=310,y=360)
        
        
        self.btn=Button(self.frame,text="Submit",fg="#FF9933",bg="black",font=('Cooper Black',22),command=self.add)
        self.btn.place(x=310,y=450)

        self.tk.mainloop()

    def add(self):
        data=(self.e1.get(),
        self.e2.get(),
        self.dob.get(),
        self.e4.get(),
        )
        if(self.e1.get()!="" and self.e1.get()!=0 and self.e2.get()!=0 and self.dob.get()!=0 and self.e4.get()!=0):
             y=database_queries.database()
             y.add_appoint(data)
            
        else:
            print("Please enter all fields")
            
   
       

