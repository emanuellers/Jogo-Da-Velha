from tkinter import *
from coresTamanhos import *
import sys
sys.path.append ('/TestandoModulos/')
from Configuracao import *
sys.path.append('/TestandoModulos/CriarJogo')
import CriarJogo

def menuIncial():
    global centro
    centro = Frame(bg= backgroundColor)#Área principal da aba

    global tituloJogo
    tituloJogo = Label(centro, text="Jogo da Velha 1.0", bg=backgroundColor, font=(fontPressStart, 20))

    global novoJogoButton
    novoJogoButton = Button(centro, text="Começar", height=2, width=20,command = lambda:comecar(), font=(fontPressStart, 15))

    global configuracao
    configuracao = Button(centro, text="Personalizar", height=2, width=20, command= lambda:personalizar(), font=(fontPressStart, 15))

    global github
    github = Button(centro, text="gitHub", height=2, width=12, font=(fontPressStart, 5), border=0)


def criarMenuInicial(boolean):
    menuIncial()
    centro.grid(row=7, column=10)
    tituloJogo.grid(row=1, column=2)
    novoJogoButton.grid(row=3, column=2)
    configuracao.grid(row=5, column=2)
    github.grid(row=10, column=3)

def fecharMenuInicial():
    centro.grid_forget()


def personalizar():
    fecharMenuInicial()
    criarMenuConfiguracoes(True)
    
def comecar():
    fecharMenuInicial()
    CriarJogo.criarPartidaJogo()
    
    
    
  






