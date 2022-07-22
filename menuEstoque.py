import operacao
import this
import os

this.loginn = ""
this.senhaa = ""
this.opcao = -1

class bcolors:
    WHITE = '\033[1;97m' #Branco
    BLACK = '\033[1;30m' #Preto
    GREEN = '\033[92m' #Verde
    YELLOW = '\033[93m' # Amarelo
    RED = '\033[91m' #Vermelho
    RESET = '\033[0m' #Resetar a Cor

def menu():
    print('|--------------------------------------|')
    print('|          ESCOLA SANTA LUZIA          |\n' +
          '|--------------------------------------|\n\n'
          'Escolha uma das opções abaixo: \n\n' +
          '1. Login\n'                                         +
          '0. Sair\n')
    this.opcao = int(input('Escolha uma opção: '))

def operar():
    while (this.opcao != 0):
        menu()
        if this.opcao == 0:
            print('\n')
            print(f"{bcolors.RED}FLW MENOR{bcolors.RESET}")

        elif this.opcao == 1:
            print('\nDigite seu Login: ')
            this.loginn = input()
            print('Digite sua Senha: ')
            this.senhaa = input()
            operacao.login(this.loginn, this.senhaa)


