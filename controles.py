import tkinter as tk
from tkinter import ttk
import time
from db import Database
db=Database("stockage.db")
def main():
    root=tk.Tk()
    app=Control(root)
    root.mainloop()
    
class Control:
    def __init__(self,master):
        self.master=master
        self.master.title("Creer compte")
        self.master.resizable(0,0)
        self.master.geometry("550x550+0+0")
        self.lbl_cmpt=tk.Label(self.master,text="Enregistrement",
        font=("time",12),fg="gray3").place(x=5,y=0)


        self.label_name=ttk.Label(self.master,text=" Nom : ")
        self.label_name.place(x=10,y=25)

        self.Entry_name=ttk.Entry(self.master)
        self.Entry_name.place(x=55,y=25,width=250)

        self.label_genre=ttk.Label(self.master,text="Genre")
        self.label_genre.place(x=10,y=55)

        self.Entry_genre=ttk.Combobox(self.master,values=["","M","F"],state="readonly")
        self.Entry_genre.place(x=55,y=55,width=150)
        self.Entry_genre.current(0)
        

        self.label_code=ttk.Label(self.master,text="Code")
        self.label_code.place(x=10,y=90)

        self.Entry_code=ttk.Entry(self.master)
        self.Entry_code.place(x=65,y=90,width=150)

        self.label_balance=ttk.Label(self.master,text="Balance")
        self.label_balance.place(x=10,y=115)

        self.Entry_balance=tk.Label(self.master,bg="white")
        self.Entry_balance.place(x=65,y=115,width=150)
        self.Entry_balance.config(text="0.0")
        

        self.label_date=ttk.Label(self.master,text="Date")
        self.label_date.place(x=10,y=155)
        self.Entry_date=tk.Label(self.master,bg="white")
        self.Entry_date.place(x=65,y=155,width=150)
        self.Entry_date.config(text=time.strftime("%d/%m/%Y"))

        btn_insert=ttk.Button(self.master,text="liste des clients",
                              command=self.ajouter)
        
        btn_insert.place(x=225,y=155)

        
        

        self.treev=ttk.Treeview(self.master,column=("ID","Nom","Genre","Code","Balance","Date"),height=18,show="headings")
        self.treev.column("ID",width=50,anchor=tk.CENTER)
        self.treev.column("Nom",width=120,anchor=tk.CENTER)
        self.treev.column("Genre",width=50,anchor=tk.CENTER)
        self.treev.column("Code",width=100,anchor=tk.CENTER)
        self.treev.column("Balance",width=70,anchor=tk.CENTER)
        self.treev.column("Date",width=70,anchor=tk.CENTER)

        self.treev.heading("ID",text="ID")
        self.treev.heading("Nom",text="Nom")
        self.treev.heading("Genre",text="Genre")
        self.treev.heading("Code",text="Code")
        self.treev.heading("Balance",text="Balance")
        self.treev.heading("Date",text="Date")
                                

        self.scrolled=tk.Scrollbar(self.master)
        self.scrolled.place(x=500,y=185)
        self.treev.configure(yscrollcommand=self.scrolled.set)
        self.scrolled.configure(command=self.treev.yview)
        
                                   
        self.treev.place(x=15,y=185,width=485)

    def ajouter(self):
        
        [self.treev.delete(i)for i in self.treev.get_children()]
        [self.treev.insert("","end",values=row)for row in db.fetch()]
        
    
                              
    

   
        
            
        
               


            
    
        
        
       
































if __name__=='__main__':
    main()
    
