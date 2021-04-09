import sys
sys.path.append ('/TestandoModulos/')
from Configuracao import *
sys.path.append('/TestandoModulos/CriarJogo')
import CriarJogo
import webbrowser

def menuIncial():
    global centro
    centro = Frame(bg= backgroundColor)#Área principal da aba

    global tituloJogo
    tituloJogo = Label(centro, text="#Jogo da Velha#", bg=backgroundColor, fg=jogoNomeCor, font=(fontPressStart, 23), pady= padYJogoNome, padx=padXJogoNome)

    global novoJogoButton
    novoJogoButton = Button(centro, text="Começar", fg= jogoNomeCor,height=2, width=20,command = lambda:comecar(), font=(fontPressStart, 15), bg=corButtonMenuInicial, border=1)

    global configuracao
    configuracao = Button(centro, text="Personalizar", fg=jogoNomeCor,  height=2, width=20, command= lambda:personalizar(), font=(fontPressStart, 15), bg=corButtonMenuInicial, border=1, )

    global mundo
    mundo = Frame(centro, width=50)

    global mundoIcon
    mundoIcon = Label(mundo, text="ü", font=(fontWebdings, 20))

    global github
    github = Button(mundo, text="gitHub", height=3, width=12, font=(fontPressStart, 5), border=0)



def callback(url):
    webbrowser.open_new(url)

def criarMenuInicial(boolean):
    menuIncial()
    centro.grid(row=0, column=0)
    tituloJogo.grid(row=1, column=2)
    novoJogoButton.grid(row=6, column=2)
    configuracao.grid(row=7, column=2)
    mundo.grid(row=10, column=1, columnspan=2)
    mundoIcon.grid(row=10, column=2)
    github.grid(row=10, column=3)
    github.bind("<Button-1>", lambda e: callback("https://github.com/emanuelle04/Jogo-Da-Velha"))

def fecharMenuInicial():
    centro.grid_forget()


def personalizar():
    fecharMenuInicial()
    criarMenuConfiguracoes(True)
    
def comecar():
    fecharMenuInicial()
    CriarJogo.criarPartidaJogo()
    
    
    
  






