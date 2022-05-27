import tkinter as tk
from tkinter import ttk
from db import Database
db=Database("stockage.db")
import time

def main():
    root=tk.Tk()
    app=Service(root)
    root.mainloop()
    
class Service:
    def __init__(self,master):
        self.master=master
        self.master.resizable(0,0)
        self.mylistes=list()
        self.lbl_cmpt=tk.Label(self.master,text="Services Organisés",
        font=("time",16),fg="gray3").place(x=5,y=0)

        self.but_cmpt=ttk.Button(self.master,text="Depot",command=self.Depot_money)
        self.but_cmpt.place(x=70,y=50)

        self.but_cmpt=ttk.Button(self.master,text="Retrait",command=self.Retrait_money)
        self.but_cmpt.place(x=70,y=85)

        self.but_cmpt=ttk.Button(self.master,text="Balance",command=self.services_sold)
        self.but_cmpt.place(x=70,y=120)


        
    def Depot_money(self):
        
        self.new=tk.Toplevel(self.master)
        self.new.title("Balance")
        self.new.geometry("350x250")
        self.label_balance=tk.Label(self.new,text="Effectuer le Versement",font=("arial",12))
        self.label_balance.place(x=50,y=0)

        self.nom_label=tk.Label(self.new,text="Nom")
        self.nom_label.place(x=15,y=42)

        self.nom_tape=tk.Entry(self.new)
        self.nom_tape.place(x=70,y=42)

        self.code_label=tk.Label(self.new,text=" Code ")
        self.code_label.place(x=15,y=72)

        self.code_tape=tk.Entry(self.new,show="*")
        self.code_tape.place(x=70,y=72)

        self.notification_label=tk.Label(self.new)
        self.notification_label.place(x=15,y=162)
        
        
        
        self.nom_button=tk.Button(self.new,text="Valider",command=self.valider_depot)
        self.nom_button.place(x=205,y=40)

        self.label_sold=tk.Label(self.new,font=("arial",10))
        self.label_sold.place(x=15,y=97)
        
    def valider_depot(self):
        
            row=db.fetch()
        
            if self.nom_tape.get()=="" or self.code_tape.get()=="":
                self.notification_label.config(text="Veuillez completez les information",fg="red")
                return
                          
            global enum
            for enum in row:
                    if self.nom_tape.get()==enum[1] and self.code_tape.get()==enum[3]:
                        self.view_depot=tk.Toplevel(self.master)
                        self.view_depot.title("Formulaire de depot")
                        self.view_depot.geometry("300x250")
                        self.viewlab=tk.Label(self.view_depot,text="Montant")
                        self.viewlab.place(x=15,y=5)
                        
                        self.entrylab=tk.Entry(self.view_depot)
                        self.entrylab.place(x=68,y=5)

                        self.vienot=tk.Label(self.view_depot)
                        self.vienot.place(x=25,y=30)

                        self.actual_sold=tk.Label(self.view_depot,text=" Solde actuel "+ enum[4])
                        self.actual_sold.place(x=25,y=70)

                        self.update_sold=tk.Label(self.view_depot)
                        self.update_sold.place(x=25,y=85)

                        self.buttonview=tk.Button(self.view_depot,text="Valider",command=self.print_result)
                        self.buttonview.place(x=200,y=5)
                        self.notification_label.config(text="Chargement effectuer",fg="blue")
                        print(enum)
                        return
                   
            self.notification_label.config(text="Mot depasse incorrect",fg="red")
  
            
            
    def print_result(self):
        try:
            if self.entrylab.get()=="":
                            self.vienot.config(text="veuiller remplir un montant",fg="red")
                            return
            if float(self.entrylab.get())<=0:
                            
                            
                self.vienot.config(text="Mettez un montant superieur a zero",fg="red")
                return
                        
            else:
                    actal_sold=float(self.entrylab.get())+float(enum[4])                            
                    self.update_sold.config(text="votre solde est"+""+ str(actal_sold)+ "Dollars")
                    print( actal_sold)
                    print(enum[5])
                    db.updates(enum[0],enum[1],enum[2],enum[3],actal_sold,enum[5])
                    self.vienot.config(text="depot effectuer",fg="blue")
                            
                              
                                
        except ValueError:
            self.vienot.config(text="Veuillez saisir une valeur numerique",fg="red")
                                
                                
                    
            
    
            
    def Retrait_money(self):
        
        self.new=tk.Toplevel(self.master)
        self.new.title("Balance")
        self.new.geometry("350x250")
        self.label_retrait=tk.Label(self.new,text="Effectuer le Retrait",font=("arial",12))
        self.label_retrait.place(x=50,y=0)

        self.nom_label=tk.Label(self.new,text="Nom")
        self.nom_label.place(x=15,y=42)

        self.nom_tape=tk.Entry(self.new)
        self.nom_tape.place(x=70,y=42)

        self.code_label=tk.Label(self.new,text=" Code ")
        self.code_label.place(x=15,y=72)

        self.code_tape=tk.Entry(self.new)
        self.code_tape.place(x=70,y=72)

        self.notification_label=tk.Label(self.new)
        self.notification_label.place(x=15,y=162)
        
        
        
        self.nom_button=tk.Button(self.new,text="Valider",command=self.valider_retrait)
        self.nom_button.place(x=205,y=40)

        self.label_sold=tk.Label(self.new,font=("arial",10))
        self.label_sold.place(x=15,y=97)
        
    def valider_retrait(self):
            row=db.fetch()
            if self.nom_tape.get()=="" or self.code_tape.get()=="":
                self.notification_label.config(text="Veuillez completez les information",fg="red")
                return
                          
            global enum
            for enum in row:
                    if self.nom_tape.get()==enum[1] and self.code_tape.get()==enum[3]:
                        self.view_retrait=tk.Toplevel(self.master)
                        self.view_retrait.title("Formulaire de Retrait")
                        self.view_retrait.geometry("300x250")
                        self.viewlab=tk.Label(self.view_retrait,text="Montant")
                        self.viewlab.place(x=15,y=5)
                        
                        self.entry_retrait=tk.Entry(self.view_retrait)
                        self.entry_retrait.place(x=68,y=5)

                        self.vienot=tk.Label(self.view_retrait)
                        self.vienot.place(x=25,y=30)

                        self.actual_sold=tk.Label(self.view_retrait,text=" Solde actuel "+ enum[4])
                        self.actual_sold.place(x=25,y=70)

                        self.update_sold=tk.Label(self.view_retrait)
                        self.update_sold.place(x=25,y=85)

                        self.buttonview=tk.Button(self.view_retrait,text="Valider",command=self.retrait_result)
                        self.buttonview.place(x=200,y=5)
                        
                        self.notification_label.config(text="Chargement effectuer",fg="blue")
                        print(enum)
                        return
                   
                    else:
                        self.notification_label.config(text="Mot depasse incorrect",fg="red")
    def retrait_result(self):
        try:
            if  self.entry_retrait.get()=="":
                            self.vienot.config(text="veuiller remplir un montant",fg="red")
                            return
            if float(self.entry_retrait.get())<=0:
                            
                 self.vienot.config(text="Mettez un montant superieur a zero",fg="red")
                 return
            if float(self.entry_retrait.get())>=float(enum[4]):
                
                self.vienot.config(text="Votre solde est insuffisant",fg="red")
                return                                           
                        
            else:
                reduice_sold=float(enum[4])-float(self.entry_retrait.get())                            
                self.update_sold.config(text="votre solde est"+""+ str(reduice_sold)+ "Dollars")
                print( reduice_sold)
                print(enum[5])
                db.updates(enum[0],enum[1],enum[2],enum[3],reduice_sold,enum[5])
                self.vienot.config(text="Depot effectuer",fg="blue")
                
        except ValueError :
                            
            self.vienot.config(text="Veuiilez saisir une valeur numerique",fg="red")
            
                                                     
                    
                        
   
            
            
                        
                        
                    
             
        
        
    def services_sold(self):
        
        self.new=tk.Toplevel(self.master)
        self.new.title("Balance")
        self.new.geometry("350x250")
        self.label_balance=tk.Label(self.new,text="Voir Balance",font=("arial",13))
        self.label_balance.place(x=50,y=0)

        self.nom_label=tk.Label(self.new,text="Nom")
        self.nom_label.place(x=15,y=42)

        self.nom_tape=tk.Entry(self.new)
        self.nom_tape.place(x=70,y=42)
        
        self.nom_button=tk.Button(self.new,text="recherche",command=self.pop)
        self.nom_button.place(x=205,y=40)
       
        self.label_motpass=tk.Label(self.new,font=("arial",10),text="Code")
        self.label_motpass.place(x=15,y=70)

        self.Entry_motpass=tk.Entry(self.new,font=("arial",10),show="*")
        self.Entry_motpass.place(x=70,y=70)

        self.label_notif=tk.Label(self.new,font=("arial",10))
        self.label_notif.place(x=25,y=110)

        self.label_sold=tk.Label(self.new,font=("arial",10))
        self.label_sold.place(x=25,y=140)
       
            
    
    def pop(self):
        
        row=db.fetch()
      
        for enum in  row:
            if self.nom_tape.get()==enum[1] and self.Entry_motpass.get()==enum[3] :
                print(enum)
                self.label_notif.config(text="BienVenue  " + self.nom_tape.get(),fg="blue")
                self.label_sold.config(text="Votre solde est de : " +(enum[4])+"Dollars")
                return
            elif self.nom_tape.get()==enum[1] and self.Entry_motpass.get()!=enum[3]:
                 self.label_notif.config(text="Mot de passe incorrect" + self.nom_tape.get(),fg="red")
                 return
               
                
            else:
                self.label_notif.config(text="pas de compte creer sous " + self.nom_tape.get(),fg="red")
            
            

        
    
    
          



















            

          
            
                                              
      
           
        
            
            
                
          
               
                
                
            
            
                    
            
            
           
                      
      
        
        
         
































if __name__=='__main__':
    main()
    
