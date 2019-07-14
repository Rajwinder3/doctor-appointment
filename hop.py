from tkinter import *
import db_queries

class main:
    def __init__(self,id_):
        print(id_)
        o=db_queries.database()
        rec=o.get_p_byid(id_)
        print(rec)
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
        self.img=PhotoImage(file="./image/img2.gif")
        self.can.create_image(0,0,image=self.img,anchor=NW)



        self.name=StringVar(self.tk)
        self.name.set(rec[1])
        
        self.can.create_text(360,100,text="Patient History",fill="#FFA833",font=('Cooper Black',35))
        
        self.can.create_text(175,220,text="Patient Name",fill="#99ccff",font=('Cooper Black',25))
        self.e1=Entry(self.frame,font=('Cooper Black',18),borderwidth="2",textvariable=self.name)
        self.e1.place(x=310,y=210)

        
        self.gen=StringVar(self.tk)
        self.gen.set(rec[2])
        self.can.create_text(175,270,text="Gender",fill="#99ccff",font=('Cooper Black',25))
        self.var = IntVar()
        self.r=Radiobutton(self.frame,text="Male",padx=10,variable=self.var,value=1,fg="black",font=('Cooper Black',15),textvariable=self.gen)
        self.r.place(x=310,y=260)
        self.r=Radiobutton(self.frame,text="Female",padx=10,variable=self.var,value=2,fg="black",font=('Cooper Black',15),textvariable=self.gen)
        self.r.place(x=450,y=260)
        
        
        self.gen=StringVar(self.tk)
        self.gen.set(rec[3])
        self.can.create_text(175,320,text="Age",fill="#99ccff",font=('Cooper Black',25))
        self.e3=Entry(self.frame,font=('Cooper Black',18),borderwidth="2",textvariable=self.gen)
        self.e3.place(x=310,y=310)


        self.c=StringVar(self.tk)
        self.c.set(rec[4])
        self.can.create_text(175,370,text="Contact",fill="#99ccff",font=('Cooper Black',25))
        self.e4=Entry(self.frame,font=('Cooper Black',18),borderwidth="2",textvariable=self.c)
        self.e4.place(x=310,y=360)


        self.add=StringVar(self.tk)
        self.add.set(rec[5])
        self.can.create_text(175,420,text="Address",fill="#99ccff",font=('Cooper Black',25))
        self.e5=Entry(self.frame,font=('Cooper Black',18),borderwidth="2",textvariable=self.c)
        self.e5.place(x=310,y=410)


        self.email=StringVar(self.tk)
        self.email.set(rec[6])
        self.can.create_text(175,470,text="Email",fill="#99ccff",font=('Cooper Black',25))
        self.e6=Entry(self.frame,font=('Cooper Black',18),borderwidth="2",textvariable=self.email)
        self.e6.place(x=310,y=460)
        
        
        self.tk.mainloop()
   
      

