from tkinter import *
class main:
    def __init__(self):
        self.win=Tk()
        #9e003a
        height=self.win.winfo_screenheight()
        width=self.win.winfo_screenwidth()
        y=(height-700)//2
        x=(width-700)//2
        self.win.geometry('700x700+{}+{}'.format(str(x),str(y)))
        self.win.resizable(height=False, width=True)
        self.gender=StringVar(self.win)
        self.can=Canvas(self.win , height=900,width=900)
        self.can.pack()

        self.img=PhotoImage(file='./images/d6.png')
        self.can.create_image(0,0, image=self.img, anchor=NW)

        self.can.create_text(200,200, text="Patient name" ,font=('cooper black',20),fill="#FFCC99")
        self.e=Entry(self.can,font=('',20))
        self.e.place(x=300,y=180)

        self.can.create_text(200,260, text="Gender", font=('cooper black',20),fill="#FFCC99")

        self.e=Radiobutton(self.can,text="Male",value="M",bg="white",variable=self.gender,font=('cooper black',15),fg="#FFCC99" )
        self.e.place(x=300,y=240)
        self.e=Radiobutton(self.can,text="Female",bg="white",value="F",variable=self.gender,font=('cooper black',15),fg="#FFCC99" )
        self.e.place(x=400,y=240)
        
        self.can.create_text(200,320, text="Age", font=('cooper black',20),fill="#FFCC99")
        self.e=Entry(self.can,font=('',20))
        self.e.place(x=300,y=300)

        self.can.create_text(200,380, text="Contact", font=('cooper black',20),fill="#FFCC99")
        self.e=Entry(self.can,font=('',20))
        self.e.place(x=300,y=360)

        self.can.create_text(200,440, text="Address", font=('cooper black',20),fill="#FFCC99")
        self.e=Entry(self.can,font=('',20) )
        self.e.place(x=300,y=420)
        
        self.can.create_text(200,500, text="Email", font=('cooper black',20),fill="#FFCC99")
        self.e=Entry(self.can,font=('',20) )
        self.e.place(x=300,y=480)
        '''
        self.btn=Button(self.can, text="Update", font=('',15))
        self.btn.place(x=470,y=540)'''
        self.win.mainloop()
d=main()
