import sqlite3

class Database:
    def __init__(self,db):
        self.conn=sqlite3.connect(db)
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS data (ID INTEGER PRIMARY KEY,Nom text,Genre text,Code text,Balance text,date text)")
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT* FROM data ")
        rows=self.cur.fetchall()
        return rows
    def inserer(self,Nom,Genre,Code,Balance,date):
        self.cur.execute("INSERT INTO data VALUES (NULL,?,?,?,?,?)",(Nom,Genre,Code,Balance,date))
        self.conn.commit()
    def remove(self,ID):
        self.cur.execute("DELETE FROM data WHERE ID=?",(ID,))
        self.conn.commit()
    def updates(self,ID,Nom,Genre,Code,Balance,date):
        self.cur.execute("UPDATE data SET Nom=?,Genre=?,Code=?,Balance=?,date=? WHERE ID=? ",(Nom,Genre,Code,Balance,date,ID))
        self.conn.commit()


def __del__(self):
    self.conn.close()
db=Database("stockage.db")
        
    
    
                         
                         
     
               
                        
                         
                    
    
