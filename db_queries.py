import mysql.connector

class database:
    def __init__(self):
        self.mydb = mysql.connector.connect(user = "root",passwd = "",host="localhost",database = "doctor_databse",)
        self.cursor = self.mydb.cursor()

    def add_patient(self,tup):
        self.cursor.execute("""INSERT INTO `patient`(`name`,`gender`,`age`,`contact`,`address`,`email`)
                            VALUES(%s,%s,%s,%s,%s,%s)""",tup)
        self.mydb.commit()

    def view_patient(self):
        self.cursor.execute("""SELECT * FROM `patient`""")
        return (self.cursor.fetchall())

    def add_appoint(self,tup):
        self.cursor.execute("""INSERT INTO `appointment`(`name`,`timing`,`date`,`description`) VALUES(%s,%s,%s,%s)""",tup)
        self.mydb.commit()

    def view_appoint(self):
        self.cursor.execute("""SELECT * FROM `appointment`""")
        return (self.cursor.fetchall())
    
    def login(self,tup):
        self.cursor.execute("""SELECT * FROM `receptionist` where email=%s and password=%s""",tup)
        return (self.cursor.fetchall())

    def get_patient_byid(self,id_):
        self.cursor.execute("SELECT * FROM `patient` where `petient_id`=%s",(id_,))
        return(self.cursor.fetchone())

    def get_appoint_byn(self,n_):
        self.cursor.execute("SELECT * FROM `appointment` where `id`=%s",(n_,))
        return(self.cursor.fetchone())

    
    def get_p_byid(self,id_):
        self.cursor.execute("SELECT * FROM `patient` where `petient_id`=%s",(id_,))
        return(self.cursor.fetchone())


    def update_appoint(self,n_):
        self.cursor.execute("UPDATE `appointment` SET `name`=%s,`timing`=%s,`date`=%s,`description`=%s WHERE `id`=%s",(n_,))
        self.mydb.commit()

   


     

    
    
        
           

