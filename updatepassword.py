from tkinter import *
import database_queries

class main:
    def __init__(self):
        self.tk=Tk()
        self.tk.geometry("700x700")
        height=self.tk.winfo_screenheight()
        width=self.tk.winfo_screenwidth()
        y=(height-700)//2
        x=(width-700)//2
        self.tk.geometry('700x700+'+str(x)+'+'+str(y))
        self.tk.resizable(height=False,width=False)

        self.f=Frame(self.tk,height="700",width="700",bg="red")
        self.f.place(x=0,y=0)

        self.f1=Frame(self.tk,height="100",width="700",bg="pink")
        self.f1.place(x=0,y=30)
        
        self.f2=Frame(self.tk,height="30",width="700",bg="black")
        self.f2.place(x=0,y=140)


        self.l=Label(self.f1,text="Update Password",fg="black",font=('cooper black',30),bg="pink")
        self.l.place(x=180,y=20)
                
        self.can=Canvas(self.f,height="700",width="700")
        self.can.pack()
        self.img=PhotoImage(file="./images/img20.gif")
        self.can.create_image(0,0,image=self.img,anchor=NW)
        self.can.create_text(200,300,text="Old Password",fill="white",font=('cooper black',25))
        self.e1=Entry(self.can,font=('cooper black',18),borderwidth="2")
        self.e1.place(x=360,y=285)
        
        self.can.create_text(200,370,text="New Password",fill="white",font=('cooper black',25))
        self.e2=Entry(self.can,font=('cooper black',18),borderwidth="2")
        self.e2.place(x=360,y=355)

        self.btn=Button(self.can,text="Update",fg="black",bg="pink",font=('Cooper Black',25),command=self.update)
        self.btn.place(x=350,y=430)

        self.tk.mainloop()
    def update(self):
        print("update")
        w=database_queries.database()
        w.update_password()

d=main()        
