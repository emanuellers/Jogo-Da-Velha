from tkinter import *
from coresTamanhos import *
import sys
sys.path.append ('/TestandoModulos/')
import Configuracao
sys.path.append('/TestandoModulos/CriarJogo')
import CriarJogo

def menuIncial():
    global centro
    centro = Frame(bg= backgroundColor)#Área principal da aba

    global tituloJogo
    tituloJogo = Label(centro, text="Jogo da Velha 1.0", bg=backgroundColor)

    global novoJogoButton
    novoJogoButton = Button(centro, text="Começar", height=2, width=20,command = lambda:comecar())

    global configuracao
    configuracao = Button(centro, text="Personalizar", height=2, width=20, command= lambda:personalizar())


def criarMenuInicial(boolean):
    menuIncial()
    centro.grid(row=7, column=10, pady=padyMenuInicialFrame, padx=padxMenuInicialFrame)
    tituloJogo.grid(row=1, column=2, pady=20, padx=5)
    novoJogoButton.grid(row=3, column=2, pady=5, padx=5)
    configuracao.grid(row=5, column=2, pady=5, padx=5)

def fecharMenuInicial():
    centro.grid_forget()


def personalizar():
    fecharMenuInicial()
    Configuracao.criarMenuConfiguracoes(True)
    
def comecar():
    fecharMenuInicial()
    CriarJogo.criarPartidaJogo()
    
    
    
  






