from tkinter import *
import database_queries

class main:
    def __init__(self):
        self.tk=Toplevel()
        
        self.frame=Frame(self.tk,height=700,width=700,bg="#ccddff")
        self.frame.place(x=0,y=0)

        height=self.tk.winfo_screenheight()
        width=self.tk.winfo_screenwidth()
        
        y=(height-700)//2
        x=(width-700)//2
        self.tk.geometry('650x650+'+str(x)+'+'+str(y))
        
        self.tk.resizable(height=False,width=False)

        self.frame1=Frame(self.tk,height=330,width=330,bg="#99bbff")
        self.frame1.place(x=220,y=60)

        self.l1=Label(self.tk,text="Add patient",fg="navy",bg="#ccddff",font=('Cooper Black',30))
        self.l1.place(x=200,y=10)

        self.can=Canvas(self.frame1,height="200",width="200",bg="light grey")
        self.can.pack()
        self.img=PhotoImage(file="./images/img11.gif")
        self.can.create_image(0,0,image=self.img,anchor=NW)

        self.l1=Label(self.frame,text="Name",fg="black",bg="#ccddff",font=('Cooper Black',20))
        self.l1.place(x=150,y=290)
        self.e1=Entry(self.frame,font=('',18),borderwidth="2")
        self.e1.place(x=310,y=290)

        self.l1=Label(self.frame,text="Gender",fg="black",bg="#ccddff",font=('Cooper Black',20))
        self.l1.place(x=150,y=335)
        #self.e=Entry(self.frame,font=('',18),show="*",borderwidth="2")
        #self.e.place(x=310,y=380)
        self.var = StringVar()
        self.r=Radiobutton(self.frame,text="Male",padx=10,variable=self.var,value="M",fg="black",font=('Cooper Black',15))
        self.r.place(x=310,y=330)
        self.r=Radiobutton(self.frame,text="Female",padx=10,variable=self.var,value="F",fg="black",font=('Cooper Black',15))
        self.r.place(x=430,y=330)

        self.l1=Label(self.frame,text="Age",fg="black",bg="#ccddff",font=('Cooper Black',20))
        self.l1.place(x=150,y=380)
        self.e3=Entry(self.frame,font=('',18),borderwidth="2")
        self.e3.place(x=310,y=375)

        self.l1=Label(self.frame,text="Contact",fg="black",bg="#ccddff",font=('Cooper Black',20))
        self.l1.place(x=150,y=425)
        self.e4=Entry(self.frame,font=('',18),borderwidth="2")
        self.e4.place(x=310,y=425)

        self.l1=Label(self.frame,text="Address",fg="black",bg="#ccddff",font=('Cooper Black',20))
        self.l1.place(x=150,y=470)
        self.e5=Entry(self.frame,font=('',18),borderwidth="2")
        self.e5.place(x=310,y=470)

        self.l1=Label(self.frame,text="Email",fg="black",bg="#ccddff",font=('Cooper Black',20))
        self.l1.place(x=150,y=510)
        self.e6=Entry(self.frame,font=('',18),borderwidth="2")
        self.e6.place(x=310,y=520)

        self.btn=Button(self.frame,text="Submit",bd=7,bg="#4d88ff",fg="black",font=('Cooper Black',20),command=self.submit)
        self.btn.place(x=310,y=580)

        self.tk.mainloop()
    def submit(self):
        x=(self.e1.get(),
           self.var.get(),
           self.e3.get(),
           self.e4.get(),
           self.e5.get(),
           self.e6.get())

        if(self.e1.get()!="" and self.var.get!=0 and self.e3.get()!=0 and self.e4.get()!=0 and self.e5.get()!=0 and self.e6.get()!=0):
             y=database_queries.database()
             y.add_patient(x)
            
        else:
            print("Please enter all fields")
    
      
