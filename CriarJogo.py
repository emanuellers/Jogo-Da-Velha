import random
import coresTamanhos
from tkinter import messagebox
from Configuracao import *
from MenuInicial import *
import threading


def partidaJogo():
    
    global frameGeralJogo
    frameGeralJogo = Frame(bg=backgroundColor)
    
    global labelNivelEscolhido
    labelNivelEscolhido = Label(frameGeralJogo, text="Nível: %d" %getNivel(), bg=backgroundColor, width = widthLabelCriarJogo, height = heighLabelCriarJogo, font=(fontPressStart, 10), fg=titulosPartidas)

    global labelQtdaPartidas
    labelQtdaPartidas = Label(frameGeralJogo, text= "Partidas: " , bg=backgroundColor, width = widthLabelCriarJogo, height = heighLabelCriarJogo, font=(fontPressStart, 10), fg=titulosPartidas)

    global frameJogoDaVelha
    frameJogoDaVelha = Frame(frameGeralJogo, bg=backgroundColor)

    global labelPontuacao
    labelPontuacao = Label(frameGeralJogo, text="Pontuação:\nJogador: 0\nRobô: 0", bg=backgroundColor, font=(fontPressStart, 10), fg=titulosPartidas)

    global alterarConfiguracoes
    alterarConfiguracoes = Button(frameGeralJogo, text="Config.", bg="#f1faee", command=lambda:(fecharPartidaJogo(),criarMenuConfiguracoes(True)), width = widthButtonPagCriarJogo, height = heighButtonPagCriarJogo, border = 0, font=(fontPressStart, 10), fg="#1d3557")

    global buttonVoltar
    buttonVoltar = Button(frameGeralJogo, text="Sair", bg="#f1faee", command=sairDoJogo, width = widthButtonPagCriarJogo, height = heighButtonPagCriarJogo, border =0, font=(fontPressStart, 10), fg=botaoSairCor)


def criarPartidaJogo():
    partidaJogo()
    frameGeralJogo.grid(row=0, column=0)
    labelNivelEscolhido.grid(row=0, column= 0)
    labelQtdaPartidas.grid(row=0, column=1)
    frameJogo()
    labelPontuacao.grid(row=frameJogoMaisUm, column=0)
    alterarConfiguracoes.grid(row= frameJogoMaisUm, column=1)
    buttonVoltar.grid(row=frameJogoMaisUm + 1, column=1)

def frameJogo():
    frameJogoDaVelha.grid(row=1, column=0, columnspan=5)
    geraMatrizVisual()
    geraMatriz()
    numPartidas()

def fecharFrameJogo():
    frameJogoDaVelha.grid_forget()


def fecharPartidaJogo():
    frameGeralJogo.grid_forget()

def sairDoJogo():
    fecharPartidaJogo()
    MenuInicial.criarMenuInicial(True)

def numPartidas():
    coresTamanhos.partidas += 1
    labelQtdaPartidas.configure(text= "Partida: " + str(coresTamanhos.partidas))

def numPontuacao():
    coresTamanhos.pontuacao+= getNivel()
    labelPontuacao.configure(text="Pontuacao\n" + "Jogador: " + str(coresTamanhos.pontuacao) + "\nRobo:" + str(coresTamanhos.pontuacaoR))

def numPontuacaoRobo():
    coresTamanhos.pontuacaoR += getNivel()
    labelPontuacao.configure(text="Pontuacao\n" + "Jogador: " + str(coresTamanhos.pontuacao) + "\nRobo:" + str(coresTamanhos.pontuacaoR))


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
    print(matrizJogo)


def atualizaMatrizRobo(posX, posY):
    matrizJogo[posX][posY] = "1"
    print(matrizJogo)

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
    elemento.configure(bg=getCores()[1])
    elemento.configure(fg=getCores()[2])
    elemento.configure(command = "")
    elemento.configure(relief=SUNKEN)
    

def posicaoButtons(elemento):
   posX = elemento.grid_info()['row']
   posY = elemento.grid_info()['column']
   jogadaPlayer(elemento)
   atualizaMatrizJogador(posX, posY)
   if matrizParaString().count("A") > 0:
       jogadaRobo()
   else:
       if conferirResultado(matrizParaString(), getNivel()) == True:
           conferirResultado(matrizParaString(), getNivel())
       else:
           empate()


   return "%s %s" %(posX, posY)

def jogadaRobo():
    relacao = []
    for i in matrizJogo:
        opcao = []
        for j in range(len(i)):
            if i[j] != "1" and i[j] != "0":
                opcao += [j]
        relacao += [opcao]
    print(relacao)

    linhas =[]
    for i in range(len(relacao)):
        if relacao[i] !=[]:
            linhas +=[i]
    escolhaLinha = random.choice(linhas)#naovazia
    print("Escolha Linha: %d \n" %escolhaLinha)
    escolhaColuna = random.choice(relacao[escolhaLinha])
    print("Escolha Coluna: %d \n"%escolhaColuna)

    puloNivel = getNivel()
    gridElemento = (puloNivel  * escolhaLinha) + escolhaColuna + 1
    print("Grid Elemento: %d" %gridElemento)
    buttonRoboJogada = listaGridJogo[gridElemento -1]
    buttonRoboJogada.configure(text=robo)
    buttonRoboJogada.configure(relief=SUNKEN)
    buttonRoboJogada.configure(command = "")
    buttonRoboJogada.configure(fg=corButtonRobo)
    atualizaMatrizRobo(escolhaLinha, escolhaColuna)
    conferirResultado(matrizParaString(), getNivel())






def conferirResultado(matrizString, nivel):
    a = 0
    if nivel == 3:
        return conferirNivelTres(matrizString)

    elif nivel == 4:
        return conferirNivelQuatro(matrizString)

    elif nivel == 5:
        return conferirNivelCinco(matrizString)


def conferirNivelTres(matrizString):
    fim = False

    diagonal = matrizString[0] + matrizString[4] + matrizString[8]

    diagonalContraria = matrizString[2] + matrizString[4] + matrizString[6]

    horizontalLinhaUm = matrizString[0] + matrizString[1] + matrizString[2]

    horizontalLinhaDois = matrizString[3] + matrizString[4] + matrizString[5]

    horizontalLinhaTres = matrizString[6] + matrizString[7] + matrizString[8]

    verticalLinhaUm = matrizString[0] + matrizString[3] + matrizString[6]

    verticalLinhaDois = matrizString[1] + matrizString[4] + matrizString[7]

    verticalLinhaTres = matrizString[2] + matrizString[5] + matrizString[8]

    if diagonal == "000" or diagonal == "111":
        fim = True
        fecharFrameJogo()
        if diagonal == "000":
            numPontuacao()
            criarFrameJogadorVenceu()
        else:
            criarFrameRoboVenceu()
            numPontuacaoRobo()

    elif diagonalContraria == "000" or diagonalContraria == "111":
        fim = True
        fecharFrameJogo()
        if diagonalContraria == "000":
            numPontuacao()
            criarFrameJogadorVenceu()
        else:
            criarFrameRoboVenceu()
            numPontuacaoRobo()

    elif horizontalLinhaUm == "000" or horizontalLinhaUm == "111":
        fim = True
        fecharFrameJogo()
        if horizontalLinhaUm == "000":
            numPontuacao()
            criarFrameJogadorVenceu()
        else:
            criarFrameRoboVenceu()
            numPontuacaoRobo()

    elif horizontalLinhaDois == "000" or horizontalLinhaDois == "111":
        fim = True
        fecharFrameJogo()
        if horizontalLinhaDois == "000":
            numPontuacao()
            criarFrameJogadorVenceu()
        else:
            criarFrameRoboVenceu()
            numPontuacaoRobo()

    elif horizontalLinhaTres == "000" or horizontalLinhaTres == "111":
        fim = True
        fecharFrameJogo()
        if horizontalLinhaTres == "000":
            numPontuacao()
            criarFrameJogadorVenceu()
        else:
            criarFrameRoboVenceu()
            numPontuacaoRobo()

    elif verticalLinhaUm == "000" or verticalLinhaUm == "111":
        fim = True
        fecharFrameJogo()
        if verticalLinhaUm == "000":
            numPontuacao()
            criarFrameJogadorVenceu()
        else:
            criarFrameRoboVenceu()
            numPontuacaoRobo()

    elif verticalLinhaDois == "000" or verticalLinhaDois == "111":
        fim = True
        fecharFrameJogo()
        if verticalLinhaDois == "000":
            numPontuacao()
            criarFrameJogadorVenceu()
        else:
            criarFrameRoboVenceu()
            numPontuacaoRobo()

    elif verticalLinhaTres == "000" or verticalLinhaTres == "111":
        fecharFrameJogo()
        if verticalLinhaTres == "000":
            numPontuacao()
            criarFrameJogadorVenceu()
        else:
            criarFrameRoboVenceu()
            numPontuacaoRobo()

    return fim

def conferirNivelQuatro(matrizString):
    fim = False

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
        fim = True
        fecharFrameJogo()
        if diagonal == "0000":
            numPontuacao()
            criarFrameJogadorVenceu()
        else:
            criarFrameRoboVenceu()
            numPontuacaoRobo()


    elif diagonalContraria == "0000" or diagonalContraria == "1111":
        fim = True
        fecharFrameJogo()
        if diagonalContraria == "0000":
            numPontuacao()
            criarFrameJogadorVenceu()
        else:
            criarFrameRoboVenceu()
            numPontuacaoRobo()

    elif horizontalLinhaUm == "0000" or horizontalLinhaUm == "1111":
        fim = True
        fecharFrameJogo()
        if horizontalLinhaUm == "0000":
            numPontuacao()
            criarFrameJogadorVenceu()
        else:
            criarFrameRoboVenceu()
            numPontuacaoRobo()

    elif horizontalLinhaDois == "0000" or horizontalLinhaDois == "1111":
        fim = True
        fecharFrameJogo()
        if horizontalLinhaDois == "0000":
            numPontuacao()
            criarFrameJogadorVenceu()
        else:
            criarFrameRoboVenceu()
            numPontuacaoRobo()

    elif horizontalLinhaTres == "0000" or horizontalLinhaTres == "1111":
        fim = True
        fecharFrameJogo()
        if horizontalLinhaTres == "0000":
            messagebox.showinfo("Vencedor", "Você Venceu o Robô! :)")
            numPontuacao()
            frameJogo()
        else:
            criarFrameRoboVenceu()
            numPontuacaoRobo()

    elif horizontalLinhaQuatro == "0000" or horizontalLinhaQuatro == "1111":
        fim = True
        fecharFrameJogo()
        if horizontalLinhaQuatro == "0000":
            numPontuacao()
            criarFrameJogadorVenceu()
        else:
            criarFrameRoboVenceu()
            numPontuacaoRobo()

    elif verticalLinhaUm == "0000" or verticalLinhaUm == "1111":
        fim = True
        fecharFrameJogo()
        if verticalLinhaUm == "0000":
            numPontuacao()
            criarFrameJogadorVenceu()
        else:
            criarFrameRoboVenceu()
            numPontuacaoRobo()

    elif verticalLinhaDois == "0000" or verticalLinhaDois == "1111":
        fim = True
        fecharFrameJogo()
        if verticalLinhaDois == "0000":
            numPontuacao()
            criarFrameJogadorVenceu()
        else:
            criarFrameRoboVenceu()
            numPontuacaoRobo()

    elif verticalLinhaTres == "0000" or verticalLinhaTres == "1111":
        fim = True
        fecharFrameJogo()
        if verticalLinhaTres == "0000":
            numPontuacao()
            criarFrameJogadorVenceu()
        else:
            criarFrameRoboVenceu()
            numPontuacaoRobo()

    elif verticalLinhaQuatro == "0000" or verticalLinhaQuatro == "1111":
        fim = True
        fecharFrameJogo()
        if verticalLinhaQuatro == "0000":
            numPontuacao()
            criarFrameJogadorVenceu()
        else:
            criarFrameRoboVenceu()
            numPontuacaoRobo()

    return fim


def conferirNivelCinco(matrizString):
    fim = True
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
        fim = True
        fecharFrameJogo()
        if diagonal == "00000":
            numPontuacao()
            criarFrameJogadorVenceu()
        else:
            criarFrameRoboVenceu()
            numPontuacaoRobo()

    elif diagonalContraria == "00000" or diagonalContraria == "11111":
        fim = True
        fecharFrameJogo()
        if diagonalContraria == "00000":
            numPontuacao()
            criarFrameJogadorVenceu()
        else:
            criarFrameRoboVenceu()
            numPontuacaoRobo()

    elif horizontalLinhaUm == "00000" or horizontalLinhaUm == "11111":
        fim = True
        fecharFrameJogo()
        if diagonal == "00000":
            numPontuacao()
            criarFrameJogadorVenceu()
        else:
            criarFrameRoboVenceu()
            numPontuacaoRobo()

    elif horizontalLinhaDois == "00000" or horizontalLinhaDois == "11111":
        fim = True
        fecharFrameJogo()
        if horizontalLinhaDois == "00000":
            numPontuacao()
            criarFrameJogadorVenceu()
        else:
            criarFrameRoboVenceu()
            numPontuacaoRobo()

    elif horizontalLinhaTres == "00000" or horizontalLinhaTres == "11111":
        fim = True
        fecharFrameJogo()
        if horizontalLinhaTres == "00000":
            numPontuacao()
            criarFrameJogadorVenceu()
        else:
            criarFrameRoboVenceu()
            numPontuacaoRobo()

    elif horizontalLinhaQuatro == "00000" or horizontalLinhaQuatro == "11111":
        fim = True
        fecharFrameJogo()
        if horizontalLinhaQuatro == "00000":
            numPontuacao()
            criarFrameJogadorVenceu()
        else:
            criarFrameRoboVenceu()
            numPontuacaoRobo()

    elif horizontalLinhaCinco == "00000" or horizontalLinhaCinco == "11111":
        fim = True
        fecharFrameJogo()
        if horizontalLinhaCinco == "00000":
            numPontuacao()
            criarFrameJogadorVenceu()
        else:
            criarFrameRoboVenceu()
            numPontuacaoRobo()

    elif verticalLinhaUm == "00000" or verticalLinhaUm == "11111":
        fim = True
        fecharFrameJogo()
        if verticalLinhaUm == "00000":
            numPontuacao()
            criarFrameJogadorVenceu()
        else:
            criarFrameRoboVenceu()
            numPontuacaoRobo()

    elif verticalLinhaDois == "00000" or verticalLinhaDois == "11111":
        fim = True
        fecharFrameJogo()
        if verticalLinhaDois == "00000":
            numPontuacao()
            criarFrameJogadorVenceu()
        else:
            criarFrameRoboVenceu()
            numPontuacaoRobo()

    elif verticalLinhaTres == "00000" or verticalLinhaTres == "11111":
        fim = True
        fecharFrameJogo()
        if verticalLinhaTres == "00000":
            numPontuacao()
            criarFrameJogadorVenceu()
        else:
            criarFrameRoboVenceu()
            numPontuacaoRobo()

    elif verticalLinhaQuatro == "00000" or verticalLinhaQuatro == "11111":
        fim = True
        fecharFrameJogo()
        if verticalLinhaQuatro == "00000":
            numPontuacao()
            criarFrameJogadorVenceu()
        else:
            criarFrameRoboVenceu()
            numPontuacaoRobo()

    elif verticalLinhaCinco == "00000" or verticalLinhaCinco == "11111":
        fim = True
        fecharFrameJogo()
        if verticalLinhaCinco == "00000":
            numPontuacao()
            criarFrameJogadorVenceu()
        else:
            criarFrameRoboVenceu()
            numPontuacaoRobo()

    return fim

def empate():
    global labelEmpate
    labelEmpate = Label(frameGeralJogo, text="Você e o Robô\nEMPATARAM", width=60, height=16, bg= backgroundColor, font=(fontPressStart, 8), fg=empatou)
    labelEmpate.grid(row=1, column=0, columnspan=5)
    start_time = threading.Timer(2, fecharEmpate)
    start_time.start()
    frameJogo()

def fecharEmpate():
    labelEmpate.grid_forget()

def criarFrameJogadorVenceu():
    global labelJogadorVenceu
    labelJogadorVenceu = Label(frameGeralJogo, text="Você derrotou o robô!\n ᕙ(`▿´)ᕗ", width=60, height=16, bg= backgroundColor, font=(fontPressStart, 8), fg=venceu)
    labelJogadorVenceu.grid(row=1, column =0, columnspan = 5)
    start_time = threading.Timer(2, fecharFrameJogadorVenceu)
    start_time.start()
    frameJogo()


def fecharFrameJogadorVenceu():
    labelJogadorVenceu.grid_forget()


def criarFrameRoboVenceu():
    global labelRoboVenceu
    labelRoboVenceu = Label(frameGeralJogo, text="OH nãaaao o Robô venceu!\n q|o~.~o|p", width=60, height=16, bg= backgroundColor, font=(fontPressStart, 8), fg=perdeu)
    labelRoboVenceu.grid(row=1, column=0, columnspan=5)
    start_time = threading.Timer(2, fecharFrameRoboVenceu)
    start_time.start()
    frameJogo()


def fecharFrameRoboVenceu():
    labelRoboVenceu.grid_forget()

''''def getInfoConfiguracao():
    try:
        getConfiguracoes()
    except:
        temaBg = corTema[0][1]
        temaFt = corTema[0][2]
        temaTexto = corTema[0][3]

    else:
        temaBg =  getConfiguracoes()[2][1]
        temaFt = getConfiguracoes()[2][1]
        temaTexto = getConfiguracoes()[2][1]

    return temaBg, temaFt, temaTexto'''''



def buttonsMatrizVisual():
    if getNivel() == 3:
        widthP = widthPartidaButtons_3 *5
        heightP = heightPartidaButtons_3*5
    elif getNivel() == 4:
        widthP = widthPartidaButtons_3 * 4
        heightP = heightPartidaButtons_3 * 4
    else:
        widthP = widthPartidaButtons_3 * 3
        heightP = heightPartidaButtons_3* 3

    gridJogo1 = Button(frameJogoDaVelha, text="¨", width=widthP, height=heightP, command=lambda: posicaoButtons(gridJogo1), bg=backgroundColor, activeforeground=activefpregroundButtons)
    gridJogo2 = Button(frameJogoDaVelha, text="¨", width=widthP, height=heightP, command=lambda: posicaoButtons(gridJogo2), bg=backgroundColor, activeforeground=activefpregroundButtons)
    gridJogo3 = Button(frameJogoDaVelha, text="¨", width=widthP, height=heightP, command=lambda: posicaoButtons(gridJogo3), bg=backgroundColor, activeforeground=activefpregroundButtons)
    gridJogo4 = Button(frameJogoDaVelha, text="¨", width=widthP, height=heightP, command=lambda: posicaoButtons(gridJogo4), bg=backgroundColor, activeforeground=activefpregroundButtons)
    gridJogo5 = Button(frameJogoDaVelha, text="¨", width=widthP, height=heightP, command=lambda: posicaoButtons(gridJogo5), bg=backgroundColor, activeforeground=activefpregroundButtons)
    gridJogo6 = Button(frameJogoDaVelha, text="¨", width=widthP, height=heightP, command=lambda: posicaoButtons(gridJogo6), bg=backgroundColor, activeforeground=activefpregroundButtons)
    gridJogo7 = Button(frameJogoDaVelha, text="¨", width=widthP, height=heightP, command=lambda: posicaoButtons(gridJogo7), bg=backgroundColor, activeforeground=activefpregroundButtons)
    gridJogo8 = Button(frameJogoDaVelha, text="¨", width=widthP, height=heightP, command=lambda: posicaoButtons(gridJogo8), bg=backgroundColor, activeforeground=activefpregroundButtons)
    gridJogo9 = Button(frameJogoDaVelha, text="¨", width=widthP, height=heightP, command=lambda: posicaoButtons(gridJogo9), bg=backgroundColor, activeforeground=activefpregroundButtons)
    gridJogo10 = Button(frameJogoDaVelha, text="¨", width=widthP, height=heightP, command=lambda: posicaoButtons(gridJogo10), bg=backgroundColor, activeforeground=activefpregroundButtons)
    gridJogo11 = Button(frameJogoDaVelha, text="¨", width=widthP, height=heightP, command=lambda: posicaoButtons(gridJogo11), bg=backgroundColor, activeforeground=activefpregroundButtons)
    gridJogo12 = Button(frameJogoDaVelha, text="¨", width=widthP, height=heightP, command=lambda: posicaoButtons(gridJogo12), bg=backgroundColor, activeforeground=activefpregroundButtons)
    gridJogo13 = Button(frameJogoDaVelha, text="¨", width=widthP, height=heightP, command=lambda: posicaoButtons(gridJogo13), bg=backgroundColor, activeforeground=activefpregroundButtons)
    gridJogo14 = Button(frameJogoDaVelha, text="¨", width=widthP, height=heightP, command=lambda: posicaoButtons(gridJogo14), bg=backgroundColor, activeforeground=activefpregroundButtons)
    gridJogo15 = Button(frameJogoDaVelha, text="¨", width=widthP, height=heightP, command=lambda: posicaoButtons(gridJogo15), bg=backgroundColor, activeforeground=activefpregroundButtons)
    gridJogo16 = Button(frameJogoDaVelha, text="¨", width=widthP, height=heightP, command=lambda: posicaoButtons(gridJogo16), bg=backgroundColor, activeforeground=activefpregroundButtons)
    gridJogo17 = Button(frameJogoDaVelha, text="¨", width=widthP, height=heightP, command=lambda: posicaoButtons(gridJogo17), bg=backgroundColor, activeforeground=activefpregroundButtons)
    gridJogo18 = Button(frameJogoDaVelha, text="¨", width=widthP, height=heightP, command=lambda: posicaoButtons(gridJogo18), bg=backgroundColor, activeforeground=activefpregroundButtons)
    gridJogo19 = Button(frameJogoDaVelha, text="¨", width=widthP, height=heightP, command=lambda: posicaoButtons(gridJogo19), bg=backgroundColor, activeforeground=activefpregroundButtons)
    gridJogo20 = Button(frameJogoDaVelha, text="¨", width=widthP, height=heightP, command=lambda: posicaoButtons(gridJogo20), bg=backgroundColor, activeforeground=activefpregroundButtons)
    gridJogo21 = Button(frameJogoDaVelha, text="¨", width=widthP, height=heightP, command=lambda: posicaoButtons(gridJogo21), bg=backgroundColor, activeforeground=activefpregroundButtons)
    gridJogo22 = Button(frameJogoDaVelha, text="¨", width=widthP, height=heightP, command=lambda: posicaoButtons(gridJogo22), bg=backgroundColor, activeforeground=activefpregroundButtons)
    gridJogo23 = Button(frameJogoDaVelha, text="¨", width=widthP, height=heightP, command=lambda: posicaoButtons(gridJogo23), bg=backgroundColor, activeforeground=activefpregroundButtons)
    gridJogo24 = Button(frameJogoDaVelha, text="¨", width=widthP, height=heightP, command=lambda: posicaoButtons(gridJogo24), bg=backgroundColor, activeforeground=activefpregroundButtons)
    gridJogo25 = Button(frameJogoDaVelha, text="¨", width=widthP, height=heightP, command=lambda: posicaoButtons(gridJogo25), bg=backgroundColor, activeforeground=activefpregroundButtons)
    global listaGridJogo
    listaGridJogo = [gridJogo1, gridJogo2, gridJogo3, gridJogo4, gridJogo5, gridJogo6, gridJogo7, gridJogo8, gridJogo9, gridJogo10, gridJogo11, gridJogo12, gridJogo13, gridJogo14, gridJogo15, gridJogo16, gridJogo17, gridJogo18, gridJogo19, gridJogo20, gridJogo21, gridJogo22, gridJogo23, gridJogo24, gridJogo25]
    return listaGridJogo



    
    
    
    
    
    
            


    
    
    

