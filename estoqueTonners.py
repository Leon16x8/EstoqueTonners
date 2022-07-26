import bdconnection
import operacao
import this
import datetime
import os

data=datetime.datetime.now()


class bcolors:
    WHITE = '\033[1;97m' #Branco
    BLACK = '\033[1;30m' #Preto
    GREEN = '\033[92m' #Verde
    YELLOW = '\033[93m' # Amarelo
    RED = '\033[91m' #Vermelho
    RESET = '\033[0m' #Resetar a Cor

def menuADM():
    print('|-----------------------------------------------------------------------|\n' +
          '|--------------------------------ESTOQUE--------------------------------|\n' +
          '|-----------------------------------------------------------------------|\n')
    print(operacao.consultarestoque())
    print('\n1. Atualizar Estoque')
    print('0. Sair\n')

    this.opcao = int(input('Qual opção deseja senhor: '))
    print('\n')

def operando():
    while (this.opcao != 0):
        menuADM()
        if this.opcao == 0:
            print('\n')
            print(f"{bcolors.RED}FLW MENOR{bcolors.RESET}")

        elif this.opcao == 1:
            print('Insira o codigo da impressora que deseja atualizar o estoque: ')
            this.codigo = input()
            print('Insira a quantidade de estoque: ')
            this.campo = input()
            operacao.atualizarEstoque('estoque' ,this.campo, this.codigo)
            os.system('cls')