from tkinter import *
import database_queries

class main:
    def __init__(self,id_):
        print(id_)
        self.id=id_
        obj=database_queries.database()
        recep=obj.get_patient_byid(id_)
        print(recep)
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

        self.can.create_text(360,100,text="Edit Patient",fill="#F1948A",font=('Cooper Black',35))

        
        self.name=StringVar(self.tk)
        self.name.set(recep[1])
        
        self.can.create_text(175,220,text="Name",fill="white",font=('Cooper Black',25))
        self.e1=Entry(self.frame,font=('Cooper Black',18),borderwidth="2",textvariable=self.name)
        self.e1.place(x=310,y=210)
        
        self.g=StringVar(self.tk,recep[2])
    
        self.can.create_text(175,270,text="Gender",fill="white",font=('Cooper Black',25))
        self.r=Radiobutton(self.frame,text="Male",padx=10,value="M",fg="black",font=('Cooper Black',15),variable=self.g)
        self.r.place(x=310,y=260)
        self.r=Radiobutton(self.frame,text="Female",padx=10,value="F",fg="black",font=('Cooper Black',15),variable=self.g)
        self.r.place(x=450,y=260)


        self.a=StringVar(self.tk)
        self.a.set(recep[3])
        self.can.create_text(175,320,text="Age",fill="white",font=('Cooper Black',25))
        self.e3=Entry(self.frame,font=('Cooper Black',18),borderwidth="2",textvariable=self.a)
        self.e3.place(x=310,y=310)



        self.c=StringVar(self.tk)
        self.c.set(recep[4])
        self.can.create_text(175,370,text="Contact",fill="white",font=('Cooper Black',25))
        self.e4=Entry(self.frame,font=('Cooper Black',18),borderwidth="2",textvariable=self.c)
        self.e4.place(x=310,y=360)


        self.add=StringVar(self.tk)
        self.add.set(recep[5])
        self.can.create_text(175,420,text="Address",fill="white",font=('Cooper Black',25))
        self.e5=Entry(self.frame,font=('Cooper Black',18),borderwidth="2",textvariable=self.add)
        self.e5.place(x=310,y=410)


        self.e=StringVar(self.tk)
        self.e.set(recep[6])
        self.can.create_text(175,470,text="Email",fill="white",font=('Cooper Black',25))
        self.e6=Entry(self.frame,font=('Cooper Black',18),borderwidth="2",textvariable=self.e)
        self.e6.place(x=310,y=460)
        
        
        self.btn=Button(self.frame,text="Update",fg="#000080",bg="#F1948A",command=self.update,font=('Cooper Black',22))
        self.btn.place(x=310,y=550)

        self.tk.mainloop()

    def update(self):
        data=[self.e1.get(),
              self.g.get(),
              self.e3.get(),
              self.e4.get(),
              self.e5.get(),
              self.e6.get(),
              self.id]
        o=database_queries.database()
        o.update_patient(data)


   
        

