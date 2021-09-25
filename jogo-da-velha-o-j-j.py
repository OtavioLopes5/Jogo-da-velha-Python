__author__ = "Otávio Lopes Fernandes"
__version__ = "1.0"
__email__ = "otaviofernandes232@gmail.com"

import time
import os
import random

def Clear(): #função para limpar o prompt/tela
    os.system('cls' if os.name == 'nt' else 'clear')

def Load(): #função inicial de "carregamento"
    Clear()
    print("Carregando.[███           ]20%")
    time.sleep(2)
    Clear()
    print("Carregando.[███████       ]50%")
    time.sleep(1)
    Clear()
    print("Carregando.[███████████   ]70%")
    time.sleep(1)
    Clear()
    print("Carregado! [██████████████]100%")
    time.sleep(1)
    Clear()

def TabelaLinha(): #função para ver a matriz com visualização de numeros nas linhas e colunas(jogo)
    print("__1___2___3_")    
    for i in range(3):
        a = 1 + i
        print(f"{a}_{mp[0][i]}_|_{mp[1][i]}_|_{mp[2][i]}_")

def Tabela(): #função para ver a matriz(jogo)
    print("___________")    
    for i in range(3):
        print(f"_{mp[0][i]}_|_{mp[1][i]}_|_{mp[2][i]}_")

def Xp(): #função para realizar o armazenamento de X na matriz
    while True: 
        try:
            colunaX = int(input("Qual coluna o X Deseja? "))
            if colunaX < 4 and colunaX > 0:
                if colunaX == 1:
                    colunaX = 0
                elif colunaX == 2:
                    colunaX = 1
                elif colunaX == 3:
                    colunaX = 2
                break
            else:
                print("Digite apenas números inteiros de 1 á 3")
        except ValueError:
                print("Digite apenas números inteiros de 1 á 3")
    while True:
        try:
            linhaX = int(input("Qual linha o X Deseja? "))
            if linhaX < 4 and linhaX > 0:
                if linhaX == 1:
                    linhaX = 0
                elif linhaX == 2:
                    linhaX = 1
                elif linhaX == 3:
                    linhaX = 2
                break
            else:
                print("Digite apenas números inteiros de 1 á 3")
        except ValueError:
            print("Digite apenas números inteiros de 1 á 3")
    if mp[colunaX][linhaX] == "X" or mp[colunaX][linhaX] == "O":
        print("Esta linha e esta coluna, já estão preenchidas. Coloque em outro lugar!") 
        Xp()
    elif mp[colunaX][linhaX]:
        mp[colunaX][linhaX] = "X" 

def Op(): #função para realizar o armazenamento de O na matriz
    while True:
        try:
            colunaO = int(input("Qual coluna o O Deseja? "))
            if colunaO < 4 and colunaO > 0:
                if colunaO == 1:
                    colunaO = 0
                elif colunaO == 2:
                    colunaO = 1
                elif colunaO == 3:
                    colunaO = 2
                break
            else:
                print("Digite apenas números inteiros de 1 á 3")
        except ValueError:
            print("Digite apenas números inteiros de 1 á 3")
    while True:
        try:        
            linhaO = int(input("Qual linha o O Deseja? "))
            if linhaO < 4 and linhaO > 0:
                if linhaO == 1:
                    linhaO = 0
                elif linhaO == 2:
                    linhaO = 1
                elif linhaO == 3:
                    linhaO = 2
                break
                
            else:
                print("Digite apenas números inteiros de 1 á 3")
        except ValueError:
            print("Digite apenas números inteiros de 1 á 3")
    if mp[colunaO][linhaO] == "X" or mp[colunaO][linhaO] == "O":
        print("Esta linha e esta coluna, já estão preenchidas. Coloque em outro lugar!") 
        Op()
    else:
        mp[colunaO][linhaO] = "O"  

def ValidResumO(): #função para parabenizar o ganhador
    Clear()
    escolhatabela()
    print("  ______        _______      ___      .__   __.  __    __    ______    __    __   __  ")
    print(" /  __  \      /  _____|    /   \     |  \ |  | |  |  |  |  /  __  \  |  |  |  | |  | ")
    print("|  |  |  |    |  |  __     /  ^  \    |   \|  | |  |__|  | |  |  |  | |  |  |  | |  | ")
    print("|  |  |  |    |  | |_ |   /  /_\  \   |  . `  | |   __   | |  |  |  | |  |  |  | |  | ")
    print("|  `--'  |    |  |__| |  /  _____  \  |  |\   | |  |  |  | |  `--'  | |  `--'  | |__| ")
    print(" \______/      \______| /__/     \__\ |__| \__| |__|  |__|  \______/   \______/  (__) \n\n")

def ValidResumX(): #função para parabenizar o ganhador
    Clear()
    escolhatabela()
    print("___   ___      _______      ___      .__   __.  __    __    ______    __    __   __  ")
    print("\  \ /  /     /  _____|    /   \     |  \ |  | |  |  |  |  /  __  \  |  |  |  | |  | ")
    print(" \  V  /     |  |  __     /  ^  \    |   \|  | |  |__|  | |  |  |  | |  |  |  | |  | ")
    print("  >   <      |  | |_ |   /  /_\  \   |  . `  | |   __   | |  |  |  | |  |  |  | |  | ")
    print(" /  .  \     |  |__| |  /  _____  \  |  |\   | |  |  |  | |  `--'  | |  `--'  | |__| ")
    print("/__/ \__\     \______| /__/     \__\ |__| \__| |__|  |__|  \______/   \______/  (__) \n\n")
    
def ValidacaoDoResultado(resultado): # valida a matriz para vefificar se o X ganhou.
    global contador_o
    global contador_x
    if mp[0][0] == "O" and  mp[1][1] == "O" and mp[2][2] == "O": #diagonal O
        ValidResumO()
        contador_o += 1
        return(resultado)
    elif mp[0][0] == "X" and  mp[1][1] == "X" and mp[2][2] == "X": #diagonal X
        ValidResumX()
        contador_x += 1
        return(resultado)
    elif mp[0][2] == "O" and  mp[1][1] == "O" and mp[2][0] == "O": #diagonal inversa O
        ValidResumO()
        contador_o += 1
        return(resultado)
    elif mp[0][2] == "X" and  mp[1][1] == "X" and mp[2][0] == "X": #diagonal inversa X
        ValidResumX()
        contador_x += 1
        return(resultado)
    elif mp[0][0] == "O" and mp[0][1] == "O" and mp[0][2] == "O": #vertical1 O
        ValidResumO()
        contador_o += 1
        return(resultado)
    elif mp[0][0] == "X" and mp[0][1] == "X" and mp[0][2] == "X": #vertical1 X
        ValidResumX()
        contador_x += 1
        return(resultado)
    elif mp[1][0] == "O" and mp[1][1] == "O" and mp[1][2] == "O": #vertical2 O
        ValidResumO()
        contador_o += 1
        return(resultado)
    elif mp[1][0] == "X" and mp[1][1] == "X" and mp[1][2] == "X": #vertical2 X
        ValidResumX()
        contador_x += 1
        return(resultado)
    elif mp[2][0] == "O" and mp[2][1] == "O" and mp[2][2] == "O": #vertical3 O
        ValidResumO()
        contador_o += 1
        return(resultado) 
    elif mp[2][0] == "X" and mp[2][1] == "X" and mp[2][2] == "X": #vertical3 X
        ValidResumX()
        contador_x += 1
        return(resultado)
    elif mp[0][0] == "O" and mp[1][0] == "O" and mp[2][0] == "O": #horizontal1 O
        ValidResumO()
        contador_o += 1
        return(resultado)
    elif mp[0][0] == "X" and mp[1][0] == "X" and mp[2][0] == "X": #horizontal1 X
        ValidResumX()
        contador_x += 1
        return(resultado)
    elif mp[0][1] == "O" and mp[1][1] == "O" and mp[2][1] == "O": #horizontal2 O
        ValidResumO()
        contador_o += 1
        return(resultado)
    elif mp[0][1] == "X" and mp[1][1] == "X" and mp[2][1] == "X": #horizontal2 X
        ValidResumX()
        contador_x += 1
        return(resultado)
    elif mp[0][2] == "O" and mp[1][2] == "O" and mp[2][2] == "O": #horizontal3 O
        ValidResumO()
        contador_o += 1
        return(resultado)
    elif mp[0][2] == "X" and mp[1][2] == "X" and mp[2][2] == "X": #horizontal3 X
        ValidResumX()
        contador_x += 1
        return(resultado)

Load()
contador_de_partidas = 0
contador_de_empates = 0
contador_o = 0 
contador_x = 0

print("Bem vindo ao jogo da velha!")
while True:
    linhasyn = ""
    linhasyn = input("Deseja ver a tabela com numeros na linha e na coluna? (S/N)").lower()
    if linhasyn == "s":
        linhasyn = "1"
        break
    elif linhasyn == "n":
        break
    else:
        print("Digite apenas S ou N.")

def escolhatabela(): #Função para escolha de tabelas numeradas ou não
    global linhasyn
    if linhasyn == "1":
        TabelaLinha()
    else:
        Tabela()

while True: # todo o jogo começa por aqui
    contador_velha = 0
    mp = [["_" for c in range(3)] for l in range(3)]

    x = random.randint(1,100)
    x = x % 2
    if x == 1:
        print("\no X é o primeiro a jogar!")
    else:
        print("\no O é o primeiro a jogar!")
    
    escolhatabela()
    while True:
        if x == 1:
            Xp()
            contador_velha += 1
            escolhatabela()
            x = 0
            acerto = ValidacaoDoResultado(1) 
        else:
            Op()
            contador_velha += 1
            escolhatabela()
            x = 1
            acerto = ValidacaoDoResultado(1) 
        
        if acerto == 1:
            contador_de_partidas += 1
            break

        if contador_velha == 9:
            Clear()
            escolhatabela()
            print(" _____                           _              __ _   _        _  _            __  ")
            print("|  ___|                         | |            / /| | | |      | || |           \ \ ")
            print("| |__   _ __ ___   _ __    __ _ | |_   ___    | | | | | |  ___ | || |__    __ _  | |")
            print("|  __| | '_ ` _ \ | '_ \  / _` || __| / _ \   | | | | | | / _ \| || '_ \  / _` | | |")
            print("| |___ | | | | | || |_) || (_| || |_ |  __/   | | \ \_/ /|  __/| || | | || (_| | | |")
            print("\____/ |_| |_| |_|| .__/  \__,_| \__| \___|   | |  \___/  \___||_||_| |_| \__,_| | |")
            print("                  | |                          \_\                              /_/ ")
            print("                  |_|                                                               \n\n")
            contador_de_empates += 1
            break

    def JogarNovamente(): #validação para o usuario jogar mais ou sair do jogo.
        print("Total de partidas:", contador_de_partidas)
        print("Total de empates: ", contador_de_empates)
        print(f"\n_____Placar_____\nX ganhou",contador_x,"vezes!\nO ganhou",contador_o,"vezes!\n")
        again = input("\nGostaria de jogar novamente? (S/N) : ").lower()
        if again == "s":
            Clear()
            pass
        else:
            print("Até mais!")
            exit()
    JogarNovamente()
    
