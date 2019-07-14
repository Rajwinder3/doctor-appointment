from tkinter import *
import database_queries
class main:
    def __init__(self):
        self.win=Toplevel()
        
        height=self.win.winfo_screenheight()
        width=self.win.winfo_screenwidth()
        y=(height-600)//2
        x=(width-600)//2
        self.win.geometry('600x600+{}+{}'.format(str(x),str(y)))
        self.win.resizable(height=False, width=True)

        self.can=Canvas(self.win , height=600,width=600)
        self.can.pack()

        self.img=PhotoImage(file='./images/d3.png')
        self.can.create_image(0,0, image=self.img, anchor=NW)
        self.gender=StringVar(self.win)
             
        self.can.create_text(150,150, text="Name", font=('cooper black',20,),fill="#FFCC66")
        self.e1=Entry(self.can,font=('',20))
        self.e1.place(x=220,y=140)

        self.can.create_text(150,200, text="Gender", font=('cooper black',20),fill="#FFCC66")

        self.var = StringVar()
         
        self.e2=Radiobutton(self.can,variable=self.var, text="Male",bg="#dac292",value="M",font=('cooper black',15),fg="#FFCC66" )
        self.e2.place(x=220,y=190)
        self.e2=Radiobutton(self.can,variable=self.var, text="Female",bg="#dac292",value="F",font=('cooper black',15),fg="#FFCC66" )
        self.e2.place(x=320,y=190)

        self.can.create_text(150,260, text="Email", font=('cooper black',20),fill="#ffcc66")
        self.e3=Entry(self.can,font=('',20))
        self.e3.place(x=220,y=240)
        
        self.can.create_text(150,320, text="Password", font=('cooper black',20),fill="#ffcc66")
        self.e4=Entry(self.can,font=('',20), show="*")
        self.e4.place(x=220,y=300)

        self.can.create_text(150,380, text="Contact", font=('cooper black',20),fill="#ffcc66")
        self.e5=Entry(self.can,font=('',20), )
        self.e5.place(x=220,y=360)

        self.can.create_text(150,440, text="Address", font=('cooper black',20),fill="#ffcc66")
        self.e6=Entry(self.can,font=('',20), )
        self.e6.place(x=220,y=420)
    
        self.btn=Button(self.can, text="Submit", font=('cooper black',15),bd=10,bg="#b37700",fg="#ffcc66", command=self.insert)
        self.btn.place(x=300,y=480)
        self.win.mainloop()

    def insert(self):
        data =(
            self.e1.get(),
            self.var.get(),
            self.e3.get(),
            self.e4.get(),
            self.e5.get(),
            self.e6.get()
        )
        if(self.e1.get()!="" and self.var.get()!="" and self.e3.get()!="" and self.e4.get()!="" and self.e5.get()!="" and self.e6.get()!=""):
             x=database_queries.database()
             x.add_receptionist(data)
        else:
            print("please enter all fields!")

