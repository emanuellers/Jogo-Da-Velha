from tkinter import *
import random
from coresTamanhos import *
from Configuracao import *
from MenuInicial import *


def partidaJogo():
    
    global frameGeralJogo
    frameGeralJogo = Frame(bg=backgroundColor)
    
    global labelNivelEscolhido
    labelNivelEscolhido = Label(frameGeralJogo, text="Nível: %d" %getNivel(), bg=backgroundColor)

    global labelQtdaPartidas
    labelQtdaPartidas = Label(frameGeralJogo, text= "Partidas: ", bg=backgroundColor)

    global frameJogoDaVelha
    frameJogoDaVelha = Frame(frameGeralJogo, bg=backgroundColor)

    global labelPontuacao
    labelPontuacao = Label(frameGeralJogo, text="Pontuação", bg=backgroundColor)

    global buttonVoltar
    buttonVoltar = Button(frameGeralJogo, text="Sair", bg=backgroundColor, command=sairDoJogo)


def criarPartidaJogo():
    partidaJogo()
    frameGeralJogo.grid(row=0, column=0, pady= 30, padx=20)
    labelNivelEscolhido.grid(row=0, column= 0, pady= 30, padx=20)
    labelQtdaPartidas.grid(row=0, column=1, pady= 30, padx=20)
    frameJogoDaVelha.grid(row=1, column=0, columnspan=3, pady= 30, padx=20)
    geraMatrizVisual()
    geraMatriz()
    labelPontuacao.grid(row=frameJogoMaisUm, column=0, pady= 30, padx=20)
    buttonVoltar.grid(row=frameJogoMaisUm, column=3, pady= 30, padx=20)

def fecharPartidaJogo():
    frameGeralJogo.grid_forget()

def sairDoJogo():
    fecharPartidaJogo()
    MenuInicial.criarMenuInicial(True)
    

def geraMatrizVisual():
    elementos = buttonsMatrizVisual()
    valores = getNivel() 
    contador = 0
    a = 0
    b = 0
    for i in range(valores):
        for j in range(valores):
            elementos[contador].grid(row=i, column=j)
            contador+=1
    
            
            


def geraMatriz():
    global matrizJogo
    valores = getNivel()
    matrizJogo = []
    for i in range(0, valores):
        lista = []
        for j in range(valores):
            lista+=[(i,j)]
        matrizJogo +=[lista]
    print(matrizJogo)
    return matrizJogo

def atualizaMatrizJogador(posX, posY):
    matrizJogo[posX][posY - 1] = 0
    
def atualizaMatrizRobo(posX, posY):
    matrizJogo[posX][posY -1] = 1
    print(matrizJogo)
    
    

def jogadaPlayer(elemento):
    elemento.configure(text= getFormatoJogador())
    elemento.configure(state=DISABLED)
    
    

    

def posicaoButtons(elemento):
   posX = elemento.grid_info()['row']
   posY = elemento.grid_info()['column']
   a = elemento.grid_info()
   jogadaPlayer(elemento)
   atualizaMatrizJogador(posX, posY)

   jogadaRobo()

   return "%s %s" %(posX, posY)

def jogadaRobo():
    relacao = []
    for i in matrizJogo:
        opcao = []
        for j in range(len(i)):
            if i[j] != 0 and i[j] != 1:
                opcao += [j]
                
        relacao += [opcao]
        
    print(relacao)
    escolhaLinha = random.randrange(len(relacao))
    print("Escolha Linha: %d" %escolhaLinha)
    escolhaColuna = random.choice(relacao[escolhaLinha]) 
    print("Escolha Coluna: %d"%escolhaColuna)

    puloNivel = getNivel()
    gridElemento = (puloNivel  * escolhaLinha) + escolhaColuna + 1
    print("Grid Elemento: %d" %gridElemento)
    buttonRoboJogada = listaGridJogo[gridElemento -1]
    buttonRoboJogada.configure(text=robo)
    buttonRoboJogada.configure(state=DISABLED)
    atualizaMatrizRobo(escolhaLinha, escolhaColuna)
    
    
    
    
                
        
        
                    #i.configure(text= robo)
                    #i.configure(state=DISABLED)
                    #atualizaMatrizRobo(jogadaRow, jogadaColumn - 1)

            
    

def buttonsMatrizVisual():
    gridJogo1 = Button(frameJogoDaVelha, text="1", width=widthPartidaButtons_3, height=heightPartidaButtons_3, command=lambda: posicaoButtons(gridJogo1))
    gridJogo2 = Button(frameJogoDaVelha, text="2", width=widthPartidaButtons_3, height=heightPartidaButtons_3, command=lambda: posicaoButtons(gridJogo2))
    gridJogo3 = Button(frameJogoDaVelha, text="3", width=widthPartidaButtons_3, height=heightPartidaButtons_3, command=lambda: posicaoButtons(gridJogo3))
    gridJogo4 = Button(frameJogoDaVelha, text="4", width=widthPartidaButtons_3, height=heightPartidaButtons_3, command=lambda: posicaoButtons(gridJogo4))
    gridJogo5 = Button(frameJogoDaVelha, text="5", width=widthPartidaButtons_3, height=heightPartidaButtons_3, command=lambda: posicaoButtons(gridJogo5))
    gridJogo6 = Button(frameJogoDaVelha, text="6", width=widthPartidaButtons_3, height=heightPartidaButtons_3, command=lambda: posicaoButtons(gridJogo6))
    gridJogo7 = Button(frameJogoDaVelha, text="7", width=widthPartidaButtons_3, height=heightPartidaButtons_3, command=lambda: posicaoButtons(gridJogo7))
    gridJogo8 = Button(frameJogoDaVelha, text="8", width=widthPartidaButtons_3, height=heightPartidaButtons_3, command=lambda: posicaoButtons(gridJogo8))
    gridJogo9 = Button(frameJogoDaVelha, text="9", width=widthPartidaButtons_3, height=heightPartidaButtons_3, command=lambda: posicaoButtons(gridJogo9))
    gridJogo10 = Button(frameJogoDaVelha, text="10", width=widthPartidaButtons_3, height=heightPartidaButtons_3, command=lambda: posicaoButtons(gridJogo10))
    gridJogo11 = Button(frameJogoDaVelha, text="11", width=widthPartidaButtons_3, height=heightPartidaButtons_3, command=lambda: posicaoButtons(gridJogo11))
    gridJogo12 = Button(frameJogoDaVelha, text="12", width=widthPartidaButtons_3, height=heightPartidaButtons_3, command=lambda: posicaoButtons(gridJogo12))
    gridJogo13 = Button(frameJogoDaVelha, text="13", width=widthPartidaButtons_3, height=heightPartidaButtons_3, command=lambda: posicaoButtons(gridJogo13))
    gridJogo14 = Button(frameJogoDaVelha, text="", width=widthPartidaButtons_3, height=heightPartidaButtons_3, command=lambda: posicaoButtons(gridJogo14))
    gridJogo15 = Button(frameJogoDaVelha, text="", width=widthPartidaButtons_3, height=heightPartidaButtons_3, command=lambda: posicaoButtons(gridJogo15))
    gridJogo16 = Button(frameJogoDaVelha, text="", width=widthPartidaButtons_3, height=heightPartidaButtons_3, command=lambda: posicaoButtons(gridJogo16))
    gridJogo17 = Button(frameJogoDaVelha, text="", width=widthPartidaButtons_3, height=heightPartidaButtons_3, command=lambda: posicaoButtons(gridJogo17))
    gridJogo18 = Button(frameJogoDaVelha, text="", width=widthPartidaButtons_3, height=heightPartidaButtons_3, command=lambda: posicaoButtons(gridJogo18))
    gridJogo19 = Button(frameJogoDaVelha, text="", width=widthPartidaButtons_3, height=heightPartidaButtons_3, command=lambda: posicaoButtons(gridJogo19))
    gridJogo20 = Button(frameJogoDaVelha, text="", width=widthPartidaButtons_3, height=heightPartidaButtons_3, command=lambda: posicaoButtons(gridJogo20))
    gridJogo21 = Button(frameJogoDaVelha, text="", width=widthPartidaButtons_3, height=heightPartidaButtons_3, command=lambda: posicaoButtons(gridJogo21))
    gridJogo22 = Button(frameJogoDaVelha, text="", width=widthPartidaButtons_3, height=heightPartidaButtons_3, command=lambda: posicaoButtons(gridJogo22))
    gridJogo23 = Button(frameJogoDaVelha, text="", width=widthPartidaButtons_3, height=heightPartidaButtons_3, command=lambda: posicaoButtons(gridJogo23))
    gridJogo24 = Button(frameJogoDaVelha, text="", width=widthPartidaButtons_3, height=heightPartidaButtons_3, command=lambda: posicaoButtons(gridJogo24))
    gridJogo25 = Button(frameJogoDaVelha, text="", width=widthPartidaButtons_3, height=heightPartidaButtons_3, command=lambda: posicaoButtons(gridJogo25))
    global listaGridJogo
    listaGridJogo = [gridJogo1, gridJogo2, gridJogo3, gridJogo4, gridJogo5, gridJogo6, gridJogo7, gridJogo8, gridJogo9, gridJogo10, gridJogo11, gridJogo12, gridJogo13, gridJogo14, gridJogo15, gridJogo16, gridJogo17, gridJogo18, gridJogo19, gridJogo20, gridJogo21, gridJogo22, gridJogo23, gridJogo24, gridJogo25]
    return listaGridJogo



    
    
    
    
    
    
            


    
    
    

