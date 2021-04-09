from MenuInicial import *
from Configuracao import *


class Aba:
    def __init__(self, toplevel):
        self.true = True
        

    def abaInicio(self):
        menuIncial()
        criarMenuInicial(True)
        

    
        
        
        
root = Tk()
root.geometry("580x450")#276x330
root.configure(bg= backgroundColor)
root.title("JogoDaVelha")
root.resizable(width= False, height=False)


aba = Aba(root)
aba.abaInicio()


root.mainloop()
        










