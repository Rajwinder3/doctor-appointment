from tkinter import *
import database_queries
class main:
    def __init__(self):
        self.win=Toplevel()
        height=self.win.winfo_screenheight()
        width=self.win.winfo_screenwidth()
        x=(height-700)//2
        y=(width-700)//2
        print(x,y)
        self.win.geometry('600x600+{}+{}'.format(str(y),str(x)))
        self.win.resizable(height=False, width=True)

        self.can=Canvas(self.win , height=700,width=700)
        self.can.pack()

        self.img=PhotoImage(file='./images/d7.png')
        self.can.create_image(0,0, image=self.img, anchor=NW)

        self.can.create_text(150,310, text="Old Password", font=('cooper black',20,"bold"),fill="white")
        self.e1=Entry(self.can,font=('',20),show="*")
        self.e1.place(x=290,y=290)

        self.can.create_text(150,390, text="New Password", font=('cooper black',20,"bold"),fill="white")
        self.e2=Entry(self.can,font=('',20), show="*")
        self.e2.place(x=290,y=370)

        self.btn=Button(self.can, text="Update", bd=10,bg="#d9c6ec",command=self.update,font=('cooper black',20), fg="white")
        self.btn.place(x=280,y=450)
       
        self.win.mainloop()
    def update(self):
        data=(self.e1.get(), self.e2.get())
        x=database_queries.database()
        x.up(data)
r=main()   

