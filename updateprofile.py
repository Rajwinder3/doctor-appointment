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

        self.f=Frame(self.tk,height="200",width="700",bg="light blue")
        self.f.place(x=0,y=0)
        '''self.l=Label(self.f,text="Update Profile",font=('cooper black',30))
        self.l.place(x=0,y=0)'''

        self.f1=Frame(self.tk,height="500",width="700",bg="red")
        self.f1.place(x=0,y=160)
        

        #self.f1=Frame(self.f,height="100",width="700",bg="light cyan")
        #self.f1.place(x=0,y=25)
        self.can=Canvas(self.f,height="200",width="700")
        self.can.pack()
        self.img=PhotoImage(file="./images/img17.gif")
        self.can.create_image(0,0,image=self.img,anchor=NW)
        self.can.create_text(350,80,text="Update Profile",fill="#FFFF99",font=('cooper black',30))
        
        self.can1=Canvas(self.f1,height="500",width="700")
        self.can1.pack()
        self.img1=PhotoImage(file="./images/img19.gif")
        self.can1.create_image(0,0,image=self.img1,anchor=NW)

        self.can1.create_text(200,100,text="Name",fill="pink",font=('cooper black',25))
        self.e1=Entry(self.can1,font=('cooper black',18),borderwidth="2")
        self.e1.place(x=300,y=90)

        self.can1.create_text(200,170,text="Email",fill="pink",font=('cooper black',25))
        self.e2=Entry(self.can1,font=('cooper black',18),borderwidth="2")
        self.e2.place(x=300,y=160)
        
        self.can1.create_text(200,240,text="Contact",fill="pink",font=('cooper black',25))
        self.e3=Entry(self.can1,font=('cooper black',18),borderwidth="2")
        self.e3.place(x=300,y=230)
        
        
        self.can1.create_text(200,320,text="Address",fill="pink",font=('cooper black',25))
        self.e4=Entry(self.can1,font=('cooper black',18),borderwidth="2")
        self.e4.place(x=300,y=310)
        


        self.btn=Button(self.can1,text="Update",command=self.update,fg="#FFFF99",bg="navy",font=('Cooper Black',22))
        self.btn.place(x=300,y=390)

        
        self.tk.mainloop()
    def update(self):
        data=[self.e1.get(),
              self.e2.get(),
              self.e3.get(),
              self.e4.get(),]
        r=database_queries.database()
        r.update_profile(data)
f=main()
        
