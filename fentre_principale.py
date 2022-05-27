import tkinter as tk
from tkinter import ttk
from service import Service
from inscriptions import Inscription
from controles import Control

def main():
    root=tk.Tk()
    app=Window1(root)
    root.mainloop()
    
class Window1:
    def __init__(self,master):
        self.master=master
        self.master.resizable(0,0)
        self.master.geometry("300x250+0+0")
        self.lbl_cmpt=tk.Label(self.master,text="Bienvenu chez Delrig Banking",
        font=("time",16),fg="gray").place(x=5,y=0)

        self.but_cmpt=ttk.Button(self.master,text="Creer un nouveau compte Courant",command=self.incripts)
        self.but_cmpt.place(x=45,y=50)

        self.but_cmpt=ttk.Button(self.master,text="Creer un nouveau compte Epargne")
        self.but_cmpt.place(x=45,y=85)

        self.but_cmpt=ttk.Button(self.master,text="    Acceder à nos Services     ",command=self.services)
        self.but_cmpt.place(x=45,y=120)

        self.but_control=ttk.Button(self.master,text=" Gestion des comptes   ",command=self.gestion_comptes)
        self.but_control.place(x=45,y=150)

    def services(self):
        self.newwindow=tk.Toplevel(self.master)
        self.app=Service(self.newwindow)
    def incripts(self):
        self.newwindow=tk.Toplevel(self.master)
        self.app=Inscription(self.newwindow)

    def gestion_comptes(self):
        self.newwindow=tk.Toplevel(self.master)
        self.app=Control(self.newwindow)
       































if __name__=='__main__':
    main()
    
