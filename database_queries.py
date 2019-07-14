import mysql.connector
 
class database:
    def __init__(self):
        self.mydb=mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="doctor_database")
        self.cursor=self.mydb.cursor()

    def add_receptionist(self,tup):
        self.cursor.execute("""insert into receptionist(`name`,`gender`,`email`,`password`,`contact`,`address`)
            values(%s,%s,%s,%s,%s,%s)""",tup)
        self.mydb.commit()
    
    def view_receptionist(self):
        self.cursor.execute("""select * from `receptionist`""")
        return(self.cursor.fetchall())
    def fetch(self,tup):
        self.cursor=self.mydb.cursor()
        self.cursor.execute("select * from `doctor` where email=%s and password=%s",tup)
        return(self.cursor.fetchall())
    def up(self,tup):
        self.cursor.execute("""update `doctor` SET `password`=%s where `email`=ranvir12@gmail.com""",tup)
        self.mydb.commit()
    def delete(self,id_):
        self.cursor.execute("""DELETE FROM `receptionist` WHERE `sn`o=%s""",(id_,))

    def get_reception_byid(self,id_):
        self.cursor.execute("SELECT * FROM `receptionist`where `sno`=%s",(id_,))
        return(self.cursor.fetchone())
    def update(self,tup):
        self.cursor.execute("""UPDATE `receptionist` SET name=%s,gender=%s,age=%s,email=%s,password=%s,contact=%s,address=%s where `sno`=%s""",tup)
        self.mydb.commit()


    def add_patient(self,tup):
        self.cursor.execute("""INSERT INTO `patient`(`name`,`gender`,`age`,`contact`,`address`,`email`)
                            VALUES(%s,%s,%s,%s,%s,%s)""",tup)
        self.mydb.commit()
    def add_appoint(self,tup):
        self.cursor.execute("""INSERT INTO `appointment`(`name`,`timing`,`date`,`description`)
                               VALUES(%s,%s,%s,%s)""",tup)
        self.mydb.commit()
    def view_appoint(self):
        self.cursor.execute("""SELECT * FROM `appointment`""")
        return (self.cursor.fetchall())
    def login(self,tup):
        self.cursor.execute("""SELECT * FROM `receptionist` where email=%s and password=%s""",tup)
        return (self.cursor.fetchall())
    def view_patient(self):
        self.cursor.execute("""SELECT * FROM `patient`""")
        return (self.cursor.fetchall())
    def get_patient_byid(self,id_):
        self.cursor.execute("SELECT * FROM `patient` where `patient_id`=%s",(id_,))
        return(self.cursor.fetchone())
    def update_patient(self,tup):
        self.cursor.execute("""UPDATE `patient` SET name=%s,gender=%s,age=%s,contact=%s,address=%s,email=%s where `patient_id`=%s""",tup)
        self.mydb.commit()
        print(self.cursor.statement)
    def get_appoint_byn(self,n_):
        self.cursor.execute("SELECT * FROM `appointment` where `id`=%s",(n_,))
        return(self.cursor.fetchone())
    def update_appoint(self,tup):
        self.cursor.execute("UPDATE `appointment` SET `name`=%s,`timing`=%s,`date`=%s,`description`=%s WHERE `id`=%s",(tup))
        self.mydb.commit()
    def update_profile(self,tup):
        self.cursor.execute("UPDATE `receptionist` SET `name`=%s,`email`=%s,`contact`=%s,`address`=%s WHERE `id`=%s",(tup))
        self.mydb.commit()

   
