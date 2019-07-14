from tkinter import *
import database_queries
class window:
    def __init__(self,id_):
        self.id=id_
        print(id_)
        obj = database_queries.database()
        recep = obj.get_reception_byid(id_)
        print(recep)
        self.win=Toplevel()
        height=self.win.winfo_screenheight()
        width=self.win.winfo_screenwidth()
        x=(width-600)//2
        y=(height-600)//2
        self.win.geometry('600x600+{}+{}'.format(str(x),str(y)))

        self.frame=Frame(self.win, height=45, width=600, bg="black")
        self.frame.place(x=0,y=0)
    
        self.frame2=Frame(self.win, height=550, width=600,bg="#a3c2c2")
        self.frame2.place(x=0,y=45)

        self.frame3=Frame(self.frame2,height=5,width=600,bg="black")
        self.frame3.place(x=0,y=5)

        self.rname = StringVar(self.win)
        self.rname.set(recep[1])
        self.name=Label(self.frame2, text="Name", bg="#a3c2c2",font=('cooper black',15))
        self.name.place(x=140,y=70)
        self.e1=Entry(self.frame2,font=('cooper black',15),textvariable=self.rname)
        self.e1.place(x=260,y=70)

        self.gen = StringVar(self.win,recep[2])
        
        
        self.gender=Label(self.frame2, text="Gender", bg="#a3c2c2",font=('cooper black',15))
        self.gender.place(x=140,y=110)
        self.g=Radiobutton(self.frame2, text="Male", value="Male",bg="#a3c2c2", font=('cooper black',15),variable=self.gen)
        self.g.place(x=260,y=110)
        self.g=Radiobutton(self.frame2, text="Female", value="Female", bg="#a3c2c2", font=('cooper black',15),variable=self.gen)
        self.g.place(x=360,y=110)

        self.em = StringVar(self.win)
        self.em.set(recep[3])
        self.email=Label(self.frame2, text="Email", bg="#a3c2c2",font=('cooper black',15))
        self.email.place(x=140,y=170)
        self.e2=Entry(self.frame2,font=('cooper black',15),textvariable=self.em)
        self.e2.place(x=260,y=170)

        self.passw = StringVar(self.win)
        self.passw.set(recep[4])
        self.password=Label(self.frame2, text="Password", bg="#a3c2c2",font=('cooper black',15))
        self.password.place(x=140,y=220)
        self.e3=Entry(self.frame2,font=('cooper black',15), show="*", textvariable=self.passw)
        self.e3.place(x=260,y=220)

        self.con = StringVar(self.win)
        self.con.set(recep[5])
        self.contact=Label(self.frame2, text="Contact", bg="#a3c2c2",font=('cooper black',15))
        self.contact.place(x=140,y=270)
        self.e4=Entry(self.frame2,font=('cooper black',15), textvariable=self.con)
        self.e4.place(x=260,y=270)

        self.add = StringVar(self.win)
        self.add.set(recep[6])
        self.address=Label(self.frame2, text="Address", bg="#a3c2c2",font=('cooper black',15))
        self.address.place(x=140,y=320)
        self.e5=Entry(self.frame2,font=('cooper black',15),textvariable=self.add )
        self.e5.place(x=260,y=320)
        
        self.frame1=Frame(self.win, height=5, width=600, bg="black")
        self.frame1.place(x=0,y=545)
        self.frame4=Frame(self.win, height=45, width=600, bg="black")
        self.frame4.place(x=0,y=555)

        self.btn=Button(self.frame2, text="Update", bd=10, activeforeground="black", command=self.update,bg="black",fg="#a3c2c2",font=('cooper black',15))
        self.btn.place(x=290,y=380)
        self.win.mainloop()
        
    def update(self):
        data=[self.e1.get(),
              self.gen.get(),
              self.e2.get(),
              self.e3.get(),
              self.e4.get(),
              self.e5.get(),
              self.id]
        r=database_queries.database()
        r.update(data)

     
