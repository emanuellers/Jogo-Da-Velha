from tkinter import *
from coresTamanhos import *
from MenuInicial import *
from Configuracao import *


class Aba:
    def __init__(self, toplevel):
        self.true =True
        

    def abaInicio(self):
        menuIncial()
        criarMenuInicial(True)
        

    
        
        
        
root = Tk()
root.geometry("600x590")#276x330
root.configure(bg= backgroundColor)
root.title("JogoDaVelha")



aba = Aba(root)
aba.abaInicio()


root.mainloop()
        









