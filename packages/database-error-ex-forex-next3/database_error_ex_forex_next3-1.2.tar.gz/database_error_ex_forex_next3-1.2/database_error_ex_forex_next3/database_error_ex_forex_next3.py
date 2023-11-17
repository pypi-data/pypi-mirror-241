import sqlite3
from sqlite3 import Error


class Database_error:

        try:
            global con
            con = sqlite3.connect('Expert_error.db')
            cur = con.cursor()
        except:
            print("connect error DB") 
        
        def sql_connection():
             try:
               con = sqlite3.connect('Expert_error.db')
               return con
             except:
              print("connect error DB") 
        
        def sql_table(con):
             cursorobj = con.cursor()
             cursorobj.execute("CREATE TABLE Epizode_error(ID integer primary key AUTOINCREMENT , candel_num text , subject text , command text )")
             con.commit()
        
        def create_table():
             cone = Database_error.sql_connection()
             Database_error.sql_table(cone)    #create database
        
        def insert_table(value):
            # try: 
               cursorobj = con.cursor()
               cursorobj.execute('INSERT INTO Epizode_error (candel_num , subject , command ) VALUES(?,?,?)', value )
               con.commit()
               print("Record INSERT successfully")
               cursorobj.close()
            # except sqlite3.Error as error:
            #    print("Failed to INSERT reocord from a sqlite table", error)    
