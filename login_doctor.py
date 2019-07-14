from tkinter import *
import database_queries

import navigation
class main:
    def __init__(self):
        self.win=Tk()
        height=self.win.winfo_screenheight()
        width=self.win.winfo_screenwidth()
        y=(height-600)//2
        x=(width-600)//2
        
        self.win.geometry('600x600+{}+{}'.format(str(x),str(y)))
        self.win.resizable(height=False, width=True)

        self.can=Canvas(self.win , height=600,width=600)
        self.can.pack()


        self.img=PhotoImage(file='./images/d2.png')
        self.can.create_image(0,0, image=self.img, anchor=NW)

        self.can.create_text(150,310, text="Email", font=('cooper black',20,))
        self.e=Entry(self.can,font=('',20))
        self.e.place(x=220,y=300)

        self.can.create_text(150,400, text="Password", font=('cooper black',20))
        self.e1=Entry(self.can,font=('',20), show="*")
        self.e1.place(x=230,y=380)

        self.btn=Button(self.can, text="Login", bd=10,bg="#ddccff", command=self.login,font=('cooper black',20))
        self.btn.place(x=300,y=450)
       
        self.win.mainloop()
    def login(self):
        data=(self.e.get(), self.e1.get())
        if(self.e.get()!="" and self.e1.get()!=""):
            y=database_queries.database()
            res=y.fetch(data)
            if res is not None:
               x=navigation.window()
            
            else:
               print("something is wrong")
        else:
             print("empty field")

        
            
d=main()
