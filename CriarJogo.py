from tkinter import *
import random
from coresTamanhos import *
from Configuracao import *
from MenuInicial import *
from tkinter import messagebox

def partidaJogo():
    
    global frameGeralJogo
    frameGeralJogo = Frame(bg=backgroundColor)
    
    global labelNivelEscolhido
    labelNivelEscolhido = Label(frameGeralJogo, text="Nível: %d" %getNivel(), bg=backgroundColor)

    global labelQtdaPartidas
    labelQtdaPartidas = Label(frameGeralJogo, text= "Partidas: " , bg=backgroundColor)

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
    frameJogo()
    labelPontuacao.grid(row=frameJogoMaisUm, column=0, pady= 30, padx=20)
    buttonVoltar.grid(row=frameJogoMaisUm, column=3, pady= 30, padx=20)

def frameJogo():
    frameJogoDaVelha.grid(row=1, column=0, columnspan=3, pady=30, padx=20)
    geraMatrizVisual()
    geraMatriz()

def fecharFrameJogo():
    frameJogoDaVelha.grid_forget()

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
    matrizJogo[posX][posY] = "0"


def atualizaMatrizRobo(posX, posY):
    matrizJogo[posX][posY] = "1"

def matrizParaString():
    matrizString = ""
    for i in matrizJogo:
        for j in i:
            valorStr = str(j)
            if "(" in valorStr:
                matrizString = matrizString + "A"
            else:
                matrizString = matrizString + valorStr
    print(matrizString)
    return matrizString


def jogadaPlayer(elemento):
    elemento.configure(text= getFormatoJogador())
    elemento.configure(state=DISABLED)
    

def posicaoButtons(elemento):
   posX = elemento.grid_info()['row']
   posY = elemento.grid_info()['column']
   jogadaPlayer(elemento)
   atualizaMatrizJogador(posX, posY)
   jogadaRobo()


   return "%s %s" %(posX, posY)

def jogadaRobo():
    relacao = []
    naoVazia = []
    for i in matrizJogo:
        opcao = []
        for j in range(len(i)):
            if i[j] != "1" and i[j] != "0":
                opcao += [j]
        relacao += [opcao]


    print(relacao)
    if relacao == [[]* getNivel()]:
        empate()
    else:
        naoVazia = []
        for i in range(len(relacao)):
            if relacao[i] != []:
                naoVazia+=[i]
        print("Não vazia: " + str(naoVazia))
        if naoVazia == []:
            empate()
        escolhaLinha = random.choice(naoVazia)
        print("Escolha Linha: %d \n" %escolhaLinha)
        escolhaColuna = random.choice(relacao[escolhaLinha])
        print("Escolha Coluna: %d \n"%escolhaColuna)

        puloNivel = getNivel()
        gridElemento = (puloNivel  * escolhaLinha) + escolhaColuna + 1
        print("Grid Elemento: %d" %gridElemento)
        buttonRoboJogada = listaGridJogo[gridElemento -1]
        buttonRoboJogada.configure(text=robo)
        buttonRoboJogada.configure(state=DISABLED)
        atualizaMatrizRobo(escolhaLinha, escolhaColuna)
        conferirResultado(matrizParaString(), getNivel())


def conferirResultado(matrizString, nivel):
    a = 0
    if nivel == 3:
        conferirNivelTres(matrizString)

    elif nivel == 4:
        conferirNivelQuatro(matrizString)

    elif nivel == 5:
        conferirNivelCinco(matrizString)


def conferirNivelTres(matrizString):

    diagonal = matrizString[0] + matrizString[4] + matrizString[8]

    diagonalContraria = matrizString[2] + matrizString[4] + matrizString[6]

    horizontalLinhaUm = matrizString[0] + matrizString[1] + matrizString[2]

    horizontalLinhaDois = matrizString[3] + matrizString[4] + matrizString[5]

    horizontalLinhaTres = matrizString[6] + matrizString[7] + matrizString[8]

    verticalLinhaUm = matrizString[0] + matrizString[3] + matrizString[6]

    verticalLinhaDois = matrizString[1] + matrizString[4] + matrizString[7]

    verticalLinhaTres = matrizString[2] + matrizString[5] + matrizString[8]

    if diagonal == "000" or diagonal == "111":
        fecharFrameJogo()
        if diagonal == "000":
            messagebox.showinfo("Vencedor", "Você Venceu o Robô! :)")
            frameJogo()
        elif diagonal == "111":
            print("Diagonal 111")
            messagebox.showinfo("Vencedor", "O Robô foi mais esperto! :(")
            frameJogo()

    elif diagonalContraria == "000" or diagonalContraria == "111":
        fecharFrameJogo()
        if diagonalContraria == "000":
            messagebox.showinfo("Vencedor", "Você Venceu o Robô! :)")
            frameJogo()
        else:
            messagebox.showinfo("Vencedor", "O Robô foi mais esperto! :(")
            frameJogo()

    elif horizontalLinhaUm == "000" or horizontalLinhaUm == "111":
        fecharFrameJogo()
        if horizontalLinhaUm == "000":
            messagebox.showinfo("Vencedor", "Você Venceu o Robô! :)")
            frameJogo()
        else:
            messagebox.showinfo("Vencedor", "O Robô foi mais esperto! :(")
            frameJogo()
    elif horizontalLinhaDois == "000" or horizontalLinhaDois == "111":
        fecharFrameJogo()
        if horizontalLinhaDois == "000":
            messagebox.showinfo("Vencedor", "Você Venceu o Robô! :)")
            frameJogo()
        else:
            messagebox.showinfo("Vencedor", "O Robô foi mais esperto! :(")
            frameJogo()
    elif horizontalLinhaTres == "000" or horizontalLinhaTres == "111":
        fecharFrameJogo()
        if horizontalLinhaTres == "000":
            messagebox.showinfo("Vencedor", "Você Venceu o Robô! :)")
            frameJogo()
        else:
            messagebox.showinfo("Vencedor", "O Robô foi mais esperto! :(")
            frameJogo()
    elif verticalLinhaUm == "000" or verticalLinhaUm == "111":
        fecharFrameJogo()
        if verticalLinhaUm == "000":
            messagebox.showinfo("Vencedor", "Você Venceu o Robô! :)")
            frameJogo()
        else:
            messagebox.showinfo("Vencedor", "O Robô foi mais esperto! :(")
            frameJogo()
    elif verticalLinhaDois == "000" or verticalLinhaDois == "111":
        fecharFrameJogo()
        if verticalLinhaDois == "000":
            messagebox.showinfo("Vencedor", "Você Venceu o Robô! :)")
            frameJogo()
        else:
            messagebox.showinfo("Vencedor", "O Robô foi mais esperto! :(")
            frameJogo()
    elif verticalLinhaTres == "000" or verticalLinhaTres == "111":
        fecharFrameJogo()
        if verticalLinhaTres == "000":
            messagebox.showinfo("Vencedor", "Você Venceu o Robô! :)")
            frameJogo()
        else:
            messagebox.showinfo("Vencedor", "O Robô foi mais esperto! :(")
            frameJogo()



def conferirNivelQuatro(matrizString):

    diagonal = matrizString[0] + matrizString[5] + matrizString[10] + matrizString[15]

    diagonalContraria = matrizString[3] + matrizString[6] + matrizString[9] + matrizString[12]

    horizontalLinhaUm = matrizString[0] + matrizString[1] + matrizString[2] + matrizString[3]

    horizontalLinhaDois = matrizString[4] + matrizString[5] + matrizString[6] + matrizString[7]

    horizontalLinhaTres = matrizString[8] + matrizString[9] + matrizString[10] + matrizString[11]

    horizontalLinhaQuatro = matrizString[12] + matrizString[13] + matrizString[14] + matrizString[15]

    verticalLinhaUm = matrizString[0] + matrizString[4] + matrizString[8] + matrizString[12]

    verticalLinhaDois = matrizString[1] + matrizString[5] + matrizString[9] + matrizString[13]

    verticalLinhaTres = matrizString[2] + matrizString[6] + matrizString[10] + matrizString[14]

    verticalLinhaQuatro = matrizString[3] + matrizString[7] + matrizString[11] + matrizString[15]

    if diagonal == "0000" or diagonal == "1111":
        fecharFrameJogo()
        if diagonal == "0000":
            messagebox.showinfo("Vencedor", "Você Venceu o Robô! :)")
            frameJogo()
        else:
            messagebox.showinfo("Vencedor", "O Robô foi mais esperto! :(")
            frameJogo()
    elif diagonalContraria == "0000" or diagonalContraria == "1111":
        fecharFrameJogo()
        if diagonalContraria == "0000":
            messagebox.showinfo("Vencedor", "Você Venceu o Robô! :)")
            frameJogo()
        else:
            messagebox.showinfo("Vencedor", "O Robô foi mais esperto! :(")
            frameJogo()

    elif horizontalLinhaUm == "0000" or horizontalLinhaUm == "1111":
        fecharFrameJogo()
        if horizontalLinhaUm == "0000":
            messagebox.showinfo("Vencedor", "Você Venceu o Robô! :)")
            frameJogo()
        else:
            messagebox.showinfo("Vencedor", "O Robô foi mais esperto! :(")
            frameJogo()
    elif horizontalLinhaDois == "0000" or horizontalLinhaDois == "1111":
        fecharFrameJogo()
        if horizontalLinhaDois == "0000":
            messagebox.showinfo("Vencedor", "Você Venceu o Robô! :)")
            frameJogo()
        else:
            messagebox.showinfo("Vencedor", "O Robô foi mais esperto! :(")
            frameJogo()
    elif horizontalLinhaTres == "0000" or horizontalLinhaTres == "1111":
        fecharFrameJogo()
        if horizontalLinhaTres == "0000":
            messagebox.showinfo("Vencedor", "Você Venceu o Robô! :)")
            frameJogo()
        else:
            messagebox.showinfo("Vencedor", "O Robô foi mais esperto! :(")
            frameJogo()
    elif horizontalLinhaQuatro == "0000" or horizontalLinhaQuatro == "1111":
        fecharFrameJogo()
        if horizontalLinhaQuatro == "0000":
            messagebox.showinfo("Vencedor", "Você Venceu o Robô! :)")
            frameJogo()
        else:
            messagebox.showinfo("Vencedor", "O Robô foi mais esperto! :(")
            frameJogo()
    elif verticalLinhaUm == "0000" or verticalLinhaUm == "1111":
        fecharFrameJogo()
        if verticalLinhaUm == "0000":
            messagebox.showinfo("Vencedor", "Você Venceu o Robô! :)")
            frameJogo()
        else:
            messagebox.showinfo("Vencedor", "O Robô foi mais esperto! :(")
            frameJogo()
    elif verticalLinhaDois == "0000" or verticalLinhaDois == "1111":
        fecharFrameJogo()
        if verticalLinhaDois == "0000":
            messagebox.showinfo("Vencedor", "Você Venceu o Robô! :)")
            frameJogo()
        else:
            messagebox.showinfo("Vencedor", "O Robô foi mais esperto! :(")
            frameJogo()
    elif verticalLinhaTres == "0000" or verticalLinhaTres == "1111":
        fecharFrameJogo()
        if verticalLinhaTres == "0000":
            messagebox.showinfo("Vencedor", "Você Venceu o Robô! :)")
            frameJogo()
        else:
            messagebox.showinfo("Vencedor", "O Robô foi mais esperto! :(")
            frameJogo()
    elif verticalLinhaQuatro == "0000" or verticalLinhaQuatro == "1111":
        fecharFrameJogo()
        if verticalLinhaQuatro == "0000":
            messagebox.showinfo("Vencedor", "Você Venceu o Robô! :)")
            frameJogo()
        else:
            messagebox.showinfo("Vencedor", "O Robô foi mais esperto! :(")
            frameJogo()


def conferirNivelCinco(matrizString):

    diagonal = matrizString[0] + matrizString[6] + matrizString[12] + matrizString[18] + matrizString[24]

    diagonalContraria = matrizString[4] + matrizString[8] + matrizString[12] + matrizString[16] + matrizString[20]

    horizontalLinhaUm = matrizString[0] + matrizString[1] + matrizString[2] + matrizString[3] + matrizString[4]

    horizontalLinhaDois = matrizString[5] + matrizString[6] + matrizString[7] + matrizString[8] + matrizString[9]

    horizontalLinhaTres = matrizString[10] + matrizString[11] + matrizString[12] + matrizString[13] + matrizString[14]

    horizontalLinhaQuatro = matrizString[15] + matrizString[16] + matrizString[17] + matrizString[18] + matrizString[19]

    horizontalLinhaCinco = matrizString[20] + matrizString[21] + matrizString[22] + matrizString[23] + matrizString[24]

    verticalLinhaUm = matrizString[0] + matrizString[5] + matrizString[10] + matrizString[15] + matrizString[20]

    verticalLinhaDois = matrizString[1] + matrizString[6] + matrizString[11] + matrizString[16] + matrizString[21]

    verticalLinhaTres = matrizString[2] + matrizString[7] + matrizString[12] + matrizString[17] + matrizString[22]

    verticalLinhaQuatro = matrizString[3] + matrizString[8] + matrizString[13] + matrizString[18] + matrizString[23]

    verticalLinhaCinco = matrizString[4] + matrizString[9] + matrizString[14] + matrizString[19] + matrizString[24]

    if diagonal == "00000" or diagonal == "11111":
        fecharFrameJogo()
        if diagonal == "00000":
            messagebox.showinfo("Vencedor", "Você Venceu o Robô! :)")
            frameJogo()
        else:
            messagebox.showinfo("Vencedor", "O Robô foi mais esperto! :(")
            frameJogo()
    elif diagonalContraria == "00000" or diagonalContraria == "11111":
        fecharFrameJogo()
        if diagonalContraria == "00000":
            messagebox.showinfo("Vencedor", "Você Venceu o Robô! :)")
            frameJogo()
        else:
            messagebox.showinfo("Vencedor", "O Robô foi mais esperto! :(")
            frameJogo()
    elif horizontalLinhaUm == "00000" or horizontalLinhaUm == "11111":
        fecharFrameJogo()
        if diagonal == "00000":
            messagebox.showinfo("Vencedor", "Você Venceu o Robô! :)")
            frameJogo()
        else:
            messagebox.showinfo("Vencedor", "O Robô foi mais esperto! :(")
            frameJogo()
    elif horizontalLinhaDois == "00000" or horizontalLinhaDois == "11111":
        fecharFrameJogo()
        if horizontalLinhaDois == "00000":
            messagebox.showinfo("Vencedor", "Você Venceu o Robô! :)")
            frameJogo()
        else:
            messagebox.showinfo("Vencedor", "O Robô foi mais esperto! :(")
            frameJogo()
    elif horizontalLinhaTres == "00000" or horizontalLinhaTres == "11111":
        fecharFrameJogo()
        if horizontalLinhaTres == "00000":
            messagebox.showinfo("Vencedor", "Você Venceu o Robô! :)")
            frameJogo()
        else:
            messagebox.showinfo("Vencedor", "O Robô foi mais esperto! :(")
            frameJogo()
    elif horizontalLinhaQuatro == "00000" or horizontalLinhaQuatro == "11111":
        fecharFrameJogo()
        if horizontalLinhaQuatro == "00000":
            messagebox.showinfo("Vencedor", "Você Venceu o Robô! :)")
            frameJogo()
        else:
            messagebox.showinfo("Vencedor", "O Robô foi mais esperto! :(")
            frameJogo()
    elif horizontalLinhaCinco == "00000" or horizontalLinhaCinco == "11111":
        fecharFrameJogo()
        if horizontalLinhaCinco == "00000":
            messagebox.showinfo("Vencedor", "Você Venceu o Robô! :)")
            frameJogo()
        else:
            messagebox.showinfo("Vencedor", "O Robô foi mais esperto! :(")
            frameJogo()
    elif verticalLinhaUm == "00000" or verticalLinhaUm == "11111":
        fecharFrameJogo()
        if verticalLinhaUm == "00000":
            messagebox.showinfo("Vencedor", "Você Venceu o Robô! :)")
            frameJogo()
        else:
            messagebox.showinfo("Vencedor", "O Robô foi mais esperto! :(")
            frameJogo()
    elif verticalLinhaDois == "00000" or verticalLinhaDois == "11111":
        fecharFrameJogo()
        if verticalLinhaDois == "00000":
            messagebox.showinfo("Vencedor", "Você Venceu o Robô! :)")
            frameJogo()
        else:
            messagebox.showinfo("Vencedor", "O Robô foi mais esperto! :(")
            frameJogo()
    elif verticalLinhaTres == "00000" or verticalLinhaTres == "11111":
        fecharFrameJogo()
        if verticalLinhaTres == "00000":
            messagebox.showinfo("Vencedor", "Você Venceu o Robô! :)")
            frameJogo()
        else:
            messagebox.showinfo("Vencedor", "O Robô foi mais esperto! :(")
            frameJogo()
    elif verticalLinhaQuatro == "00000" or verticalLinhaQuatro == "11111":
        fecharFrameJogo()
        if verticalLinhaQuatro == "00000":
            messagebox.showinfo("Vencedor", "Você Venceu o Robô! :)")
            frameJogo()
        else:
            messagebox.showinfo("Vencedor", "O Robô foi mais esperto! :(")
            frameJogo()
    elif verticalLinhaCinco == "00000" or verticalLinhaCinco == "11111":
        fecharFrameJogo()
        if verticalLinhaCinco == "00000":
            messagebox.showinfo("Vencedor", "Você Venceu o Robô! :)")
            frameJogo()
        else:
            messagebox.showinfo("Vencedor", "O Robô foi mais esperto! :(")
            frameJogo()

def empate():
    fecharFrameJogo()
    messagebox.showinfo("Empate", "Você e o Robô empataram! O.o")
    frameJogo()


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
    gridJogo14 = Button(frameJogoDaVelha, text="14", width=widthPartidaButtons_3, height=heightPartidaButtons_3, command=lambda: posicaoButtons(gridJogo14))
    gridJogo15 = Button(frameJogoDaVelha, text="15", width=widthPartidaButtons_3, height=heightPartidaButtons_3, command=lambda: posicaoButtons(gridJogo15))
    gridJogo16 = Button(frameJogoDaVelha, text="16", width=widthPartidaButtons_3, height=heightPartidaButtons_3, command=lambda: posicaoButtons(gridJogo16))
    gridJogo17 = Button(frameJogoDaVelha, text="17", width=widthPartidaButtons_3, height=heightPartidaButtons_3, command=lambda: posicaoButtons(gridJogo17))
    gridJogo18 = Button(frameJogoDaVelha, text="18", width=widthPartidaButtons_3, height=heightPartidaButtons_3, command=lambda: posicaoButtons(gridJogo18))
    gridJogo19 = Button(frameJogoDaVelha, text="19", width=widthPartidaButtons_3, height=heightPartidaButtons_3, command=lambda: posicaoButtons(gridJogo19))
    gridJogo20 = Button(frameJogoDaVelha, text="20", width=widthPartidaButtons_3, height=heightPartidaButtons_3, command=lambda: posicaoButtons(gridJogo20))
    gridJogo21 = Button(frameJogoDaVelha, text="21", width=widthPartidaButtons_3, height=heightPartidaButtons_3, command=lambda: posicaoButtons(gridJogo21))
    gridJogo22 = Button(frameJogoDaVelha, text="22", width=widthPartidaButtons_3, height=heightPartidaButtons_3, command=lambda: posicaoButtons(gridJogo22))
    gridJogo23 = Button(frameJogoDaVelha, text="23", width=widthPartidaButtons_3, height=heightPartidaButtons_3, command=lambda: posicaoButtons(gridJogo23))
    gridJogo24 = Button(frameJogoDaVelha, text="24", width=widthPartidaButtons_3, height=heightPartidaButtons_3, command=lambda: posicaoButtons(gridJogo24))
    gridJogo25 = Button(frameJogoDaVelha, text="25", width=widthPartidaButtons_3, height=heightPartidaButtons_3, command=lambda: posicaoButtons(gridJogo25))
    global listaGridJogo
    listaGridJogo = [gridJogo1, gridJogo2, gridJogo3, gridJogo4, gridJogo5, gridJogo6, gridJogo7, gridJogo8, gridJogo9, gridJogo10, gridJogo11, gridJogo12, gridJogo13, gridJogo14, gridJogo15, gridJogo16, gridJogo17, gridJogo18, gridJogo19, gridJogo20, gridJogo21, gridJogo22, gridJogo23, gridJogo24, gridJogo25]
    return listaGridJogo



    
    
    
    
    
    
            


    
    
    

