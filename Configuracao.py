from tkinter import *
from coresTamanhos import *
import MenuInicial

#configroot = Tk()
#configroot.geometry("1000x1000")#276x330
#configroot.configure(bg= "white")
#configroot.title("JogoDaVelha")

def configuracaoTela():
  global novaTela
  novaTela = Frame(bg=backgroundColor)

  global labelConfiguracao
  labelConfiguracao = Label(novaTela,text="Configurações", bg= backgroundColor, pady=padYItens)
    

  global labelDificuldade
  labelDificuldade = Label(novaTela, text="Níveis: ", bg=backgroundColor, pady=padYItens)
      

  global labelTemas
  labelTemas = Label(novaTela, text="Temas: ", bg =backgroundColor , pady=padYItens)
      

  global labelFormato
  labelFormato = Label(novaTela, text="Formato: ", bg=backgroundColor, pady=padYItens)
      
  global labelFormatoRobo
  labelFormatoRobo = Label(novaTela, text="Formato Robô:  %s" %robo, bg= backgroundColor, pady=padYItens)
      

  global salvarConfiguracoes
  salvarConfiguracoes = Button(novaTela, text="Salvar", pady=padYItens, bg= backgroundColor, width=widthSalvarConfiguracoes, command=lambda:getConfiguracoes() )
    


def criarMenuConfiguracoes(boolean):
  configuracaoTela()
  if(boolean == True):
    labelConfiguracao.grid(row=0, column =0, columnspan=3)
    novaTela.grid(row=0, column=0, columnspan=4)
    labelDificuldade.grid(row=2, column=0)
    definirNivel()
    labelTemas.grid(row=4, column= 0)
    definirCores()
    labelFormato.grid(row=6, column=0)
    definirSeuFormato()
    labelFormatoRobo.grid(row=10, columnspan= 2)
    salvarConfiguracoes.grid(row=10, column=2, columnspan=2)
  else:
    return "Not selected Configuration Menu"
    

def fecharMenuConfiguracoes(boolean):
  novaTela.grid_forget()

def definirNivel():
  global nivel 
  nivel = IntVar(None, 3)
  nivelDificuldade1 = Radiobutton(novaTela,text="3x3", value=3, variable=nivel, bg=backgroundColor, width=widthNiveis )
  nivelDificuldade2 = Radiobutton(novaTela,text="4x4", value=4, variable=nivel, bg=backgroundColor, width=widthNiveis)
  nivelDificuldade3 = Radiobutton(novaTela, text="5x5", value=5,variable=nivel, bg=backgroundColor, width=widthNiveis)
  
  nivelDificuldade1.grid(row=3, column=0)
  nivelDificuldade2.grid(row=3, column=1)
  nivelDificuldade3.grid(row=3, column=2)

def definirCores():
  temabtn1 = Button(novaTela, text = corTema[0][0], bg= corTema[0][1], fg=corTema[0][2], activebackground= corTema[0][1], activeforeground=corTema[0][2], width=widthCoresButton, command = lambda:( getCoresButton(0), alertaTema()))
  temabtn2 = Button(novaTela, text = corTema[1][0], bg= corTema[1][1], fg=corTema[1][2], activebackground= corTema[1][1], activeforeground=corTema[1][2], width=widthCoresButton, command = lambda:( getCoresButton(1), alertaTema()))
  temabtn3 = Button(novaTela, text = corTema[2][0], bg= corTema[2][1], fg=corTema[2][2], activebackground= corTema[2][1], activeforeground=corTema[2][2], width=widthCoresButton, command = lambda:( getCoresButton(2), alertaTema()))

  temabtn1.grid(row=5, column=0)
  temabtn2.grid(row=5, column=1)
  temabtn3.grid(row=5, column=2)

def alertaTema():
  temaEscolhido = "Tema: " + temaCores[0]
  labelTemasTexto = Label(novaTela, text= temaEscolhido, bg =backgroundColor, pady=padYItens)
  labelTemasTexto.grid(row=11, column=0)

def definirSeuFormato():
  global formato
  formato = StringVar(None, "X")
  forma1 = Radiobutton(novaTela, text="X", value="X", variable=formato, bg=backgroundColor, width=widthFormato)
  forma2 = Radiobutton(novaTela, text="O", value="O", variable=formato, bg=backgroundColor, width=widthFormato)
  forma3 = Radiobutton(novaTela, text=olhosFechados, value=olhosFechados,variable=formato, bg=backgroundColor, width=widthFormato)
  forma4 = Radiobutton(novaTela, text=urso, value=urso, variable=formato, bg=backgroundColor, width=widthFormato)
  forma5 = Radiobutton(novaTela, text=feliz, value=feliz, variable=formato, bg=backgroundColor, width=widthFormato)
  forma6 = Radiobutton(novaTela, text=gatinho, value=gatinho,variable=formato, bg=backgroundColor, width=widthFormato)
  

  forma1.grid(row=7, column=0)
  forma2.grid(row=7, column=1)
  forma3.grid(row=7, column=2)
  forma4.grid(row=8, column=0)
  forma5.grid(row=8, column=1)
  forma6.grid(row=8, column=2)

def getConfiguracoes():
  try:
    temaCores
  except:
    getTemaCores = corTema[0]
  else:
    getTemaCores = temaCores
  print(getNivel())
  print(getFormatoJogador())
  print(getTemaCores)
  fecharMenuConfiguracoes(True)
  MenuInicial.criarMenuInicial(True)
  listaValores = [getNivel(), getFormatoJogador(), getTemaCores]
  return listaValores

def getCoresButton(corTemaValor):
  global temaCores
  temaCores = corTema[corTemaValor]
  return temaCores

def getNivel():
  try:
    nivel.get()
    nivelEscolhido = nivel.get()
  except:
    nivelEscolhido = 3
  
  return nivelEscolhido

def getFormatoJogador():
  try:
    formato.get()
    formatoEscolhido = formato.get()
  except:
    formatoEscolhido = "X"
  return formatoEscolhido



#configroot.mainloop()
