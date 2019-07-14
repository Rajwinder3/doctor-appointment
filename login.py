from tkinter import *
import database_queries
import navigation1
class main:
    def __init__(self):
        self.tk=Tk()
        
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
        self.img=PhotoImage(file="./images/image6.gif")
        self.can.create_image(0,0,image=self.img,anchor=NW)
        self.can.create_text(175,250,text="Email",fill="black",font=('Cooper Black',25))
        self.can.create_text(210,320,text="Password",fill="black",font=('Cooper Black',25))

        '''self.l1=Label(self.can,text="Email",fg="black",bg="light grey",font=('georgia',22))
        self.l1.place(x=150,y=280)'''
        self.e1=Entry(self.frame,font=('Cooper Black',18),borderwidth="2",bg="powder blue")
        self.e1.place(x=310,y=240)

        '''self.l1=Label(self.can,text="Password",fg="black",bg="light grey",font=('georgia',22))
        self.l1.place(x=150,y=360)'''
        self.e2=Entry(self.frame,font=('Cooper Black',18),show="*",borderwidth="2",bg="powder blue")
        self.e2.place(x=310,y=305)

        self.btn=Button(self.frame,text="Login",fg="black",bg="#6699ff",font=('Cooper Black',22,'bold'),bd=7,command=self.change)
        self.btn.place(x=310,y=370)

        self.tk.mainloop()
    def change(self):
        data=(self.e1.get(), self.e2.get())
        if (self.e1.get!="" and self.e2.get()!=""):
            x=database_queries.database()
            r=x.login(data)
            if r is not None:
                y=navigation1.Main()
        else:
            print("Please login first")
        
d=main()        
