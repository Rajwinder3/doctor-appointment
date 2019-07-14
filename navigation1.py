from tkinter import *
import addpatient
import manage_p
import addappoint
import manageappointment
import updateprofile
import updatepassword
import logout
class Main:
     def __init__(self):
         self.tk=Tk()
         self.tk.geometry('700x700')
         self.tk.title("navigation")
         height=self.tk.winfo_screenheight()
         width=self.tk.winfo_screenwidth()
        
         y=(height-700)//2
         x=(width-700)//2
         self.tk.geometry('700x700+'+str(x)+'+'+str(y))
        
         self.tk.resizable(height=False,width=False)
         
         self.can=Canvas(self.tk,height="700",width="700",bg="light grey")
         self.can.pack()
         self.img=PhotoImage(file="./images/image9.gif")
         self.can.create_image(0,0,image=self.img,anchor=NW)

         self.f=Frame(self.can,height="100",width="700",bg="pink")
         self.f.place(x=0,y=0)
         
         self.menu=Menu(self.tk)
         self.sub=Menu(self.menu)
         self.sub.add_cascade(label="Add patient",font=('Cooper Black',20),command=self.add)
         self.sub.add_cascade(label="Manage patient",font=('Cooper Black',20),command=self.manage)
         self.menu.add_cascade(label="Patient",menu=self.sub)
         
         self.sub=Menu(self.menu)
         self.sub.add_cascade(label="Add",font=('Cooper Black',18),command=self.insert)
         self.sub.add_cascade(label="Manage",font=('Cooper Black',18),command=self.mappoint)
         self.menu.add_cascade(label="Appointment",menu=self.sub)
         

         self.sub=Menu(self.menu)
         self.sub.add_cascade(label="Update profile",font=('Cooper Black',18),command=self.up)
         self.sub.add_cascade(label="Update password",font=('Cooper Black',18),command=self.updatepass)
         self.sub.add_cascade(label="Logout",font=('Cooper Black',18),command=self.logout)
         self.menu.add_cascade(label="Account",menu=self.sub)
         

         self.tk.config(menu=self.menu)
         self.tk.mainloop()
     def add(self):
          e=addpatient.main()
     def manage(self):
          a=manage_p.main()
     def insert(self):
          b=addappoint.main()
     def mappoint(self):
          c=manageappointment.main()
     def up(self):
          c=updateprofile.main()
     def updatepss(self):
          c=updatepassword.main()
     def up(self):
          c=logout.main()
    
    
f=Main()
    
            
        
