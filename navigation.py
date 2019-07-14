from tkinter import *
import add_receptionist
import manage_receptionist
import update_password
import database_queries
class window:
    def __init__(self):
        self.win=Tk()
        height=self.win.winfo_screenheight()
        width=self.win.winfo_screenwidth()
        x=(width-600)//2
        y=(height-600)//2
        self.win.geometry('600x600+{}+{}'.format(str(x),str(y)))
        self.win.resizable(width=False, height=False)

        #self.frame=Frame(self.win, height=600, width=600, bg="#00e6e6")
        #self.frame.place(x=0,y=0)
        #self.frame1=Frame(self.win, height=5,width=600, bg="#008080")
        #self.frame1.place(x=0,y=0)
        self.can=Canvas(self.win , height=700,width=700)
        self.can.pack()

        self.img=PhotoImage(file='./images/d9.png')
        self.can.create_image(0,0, image=self.img, anchor=NW)
        
        self.menu=Menu(self.win)
        self.sub=Menu(self.menu)
        self.sub.add_cascade(label="Add",command=self.trigger)
        self.sub.add_cascade(label="Manage",command=self.trigger1)
        self.menu.add_cascade(label="Reception", font=('cooper black',15), menu=self.sub)

        self.sub=Menu(self.menu)
        self.sub.add_cascade(label="Today's appointment",command=self.trigger2)
        self.sub.add_cascade(label="Appointment History",command=self.trigger3)
        self.menu.add_cascade(label="Appointment", font=('cooper black',15), menu=self.sub)
        
        self.sub=Menu(self.menu)
        self.sub.add_cascade(label="Update password",command=self.trigger4)
        self.sub.add_cascade(label="Logout",command=self.trigger5)
        self.menu.add_cascade(label="Account", font=('cooper black',15), menu=self.sub)
        
        self.win.config(menu=self.menu)

        
         
        self.win.mainloop()


    def trigger(self):
        t=add_receptionist.main()
    def trigger1(self):
        t=manage_receptionist.window()
    def trigger2(self):
        t=add_receptionist.main()
    def trigger3(self):
        t=add_receptionist.main()
    def trigger4(self):
        t=update_password.main()
    def trigger5(self):
        t=database_queries.database()
        t.logout()
    
d=window()
