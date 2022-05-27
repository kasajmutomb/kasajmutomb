import tkinter as tk
from tkinter import ttk
import time
from controles import Control
from db import Database
db=Database("stockage.db")

def main():
    root=tk.Tk()
    app=Inscription(root)
    root.mainloop()
    
class Inscription:
    mylist=list()
    def __init__(self,master):
        
        self.master=master
        self.master.title("Creer compte")
        self.master.resizable(0,0)
        self.master.geometry("350x300+0+0")
        self.balance="0.0"
        self.temps=time.strftime("%d/%m/%Y")
        self.lbl_cmpt=tk.Label(self.master,text="Enregistrement",
        font=("time",12),fg="gray3").place(x=5,y=0)

        self.label_name=ttk.Label(self.master,text=" Nom: ")
        self.label_name.place(x=10,y=25)

        self.Entry_name=ttk.Entry(self.master)
        self.Entry_name.place(x=65,y=25,width=250)

        self.label_genre=ttk.Label(self.master,text="Genre")
        self.label_genre.place(x=10,y=65)

        self.Entry_genre=ttk.Combobox(self.master,values=["","M","F"],state="readonly")
        self.Entry_genre.place(x=65,y=65,width=150)
        self.Entry_genre.current(0)
        

        self.label_code=ttk.Label(self.master,text="Code")
        self.label_code.place(x=10,y=105)

        self.Entry_code=ttk.Entry(self.master)
        self.Entry_code.place(x=65,y=105,width=150)

        self.label_balance=ttk.Label(self.master,text="Balance")
        self.label_balance.place(x=10,y=145)

        self.Entry_balance=tk.Label(self.master,bg="white")
        self.Entry_balance.place(x=65,y=145,width=150)
        self.Entry_balance.config(text=self.balance)
        

        self.label_date=ttk.Label(self.master,text="Date")
        self.label_date.place(x=10,y=170)
        self.Entry_date=tk.Label(self.master,bg="white")
        self.Entry_date.place(x=65,y=170,width=150)
        self.Entry_date.config(text=self.temps)

        self.btn_valide=ttk.Button(self.master,text="Valider",command=self.valider)
        self.btn_valide.place(x=35,y=210)

        self.btn_valide=ttk.Button(self.master,text="Annuler",command=self.annuler)
        self.btn_valide.place(x=125,y=210)

        self.label_notif=tk.Label(self.master)
        self.label_notif.place(x=10,y=265)

        
        
        
        


    def valider(self):
        if   self.Entry_name.get()=="" or self.Entry_genre.get()=="" or self.Entry_code.get()=="":
            self.label_notif.config(text="Veuiilllez remplir les champs",fg="red")
            return
        else:
            db.inserer(self.Entry_name.get(),self.Entry_genre.get(),
                      self.Entry_code.get(),self.balance,self.temps)
            
            
         
            
            
            
        
            
        
    def annuler(self):
        print("Operation annuler")
































if __name__=='__main__':
    main()
    
