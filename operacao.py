import mysql.connector
import bdconnection
import estoqueTonners
import os
from datetime import date, time, datetime, timedelta
import getpass

db_connection = bdconnection.conectar()
con = db_connection.cursor()

class bcolors:
    WHITE = '\033[1;97m' #Branco
    BLACK = '\033[1;30m' #Preto
    GREEN = '\033[92m' #Verde
    YELLOW = '\033[93m' # Amarelo
    RED = '\033[91m' #Vermelho
    RESET = '\033[0m' #Resetar a Cor

def consultarLoginSenha(loginn, senhaa):
    try:
        sql = 'select login, senha from Users'
        con.execute(sql)
        for(login, senha) in con:
            if login == loginn and senha == senhaa:
                return True
        return False
    except Exception as erro:
        print(erro)

def login(loginn, senhaa):
    try:
        if consultarLoginSenha(loginn, senhaa) == True:
            print('Logado com Sucesso !')
            print('\n')
            os.system('cls')
            estoqueTonners.operando()
        else:
            print('Login e Senha incorretos!')
            os.system('cls')
            print('\n')
    except Exception as erro:
        print(erro)

def consultarestoque():
    try:
        sql = 'select codigo, impressora, estoque, preço, modifica from EstoqueBro'
        con.execute(sql)
        for(codigo, impressora, estoque, preço, modifica) in con:
            print("-----------------------------------------------")
            print('Impressora {}: {}'.format(codigo, impressora))
            print('Estoque: {}'.format(estoque))
            print('Valor do Tonner: R${}'.format(preço))
            print('Data de Modificação: {}'.format(modifica))
            if estoque == 0:
                print("Precisamos comprar mais 2 Tonners")
                print("-----------------------------------------------")
            else:
                print("Safe Familia")
                print("-----------------------------------------------")

            print(f"{bcolors.RESET}")
    except Exception as erro:
        return erro

def adicionarEstoque(estoque):
    try:
        sql = "insert into EstoqueBro(codigo, estoque) values ('{}', '{}')".format(estoque)
        con.execute(sql)
        db_connection.commit() #Inserção de dados no BD
        print("{} Produto inserido com Sucesso!\n".format(con.rowcount))
    except Exception as erro:
        return erro

def atualizarEstoque(campo, novoDado, codigo):
    try:
        data = datetime.today()
        sql = "update EstoqueBro set {} = '{}' where codigo = '{}'".format(campo, novoDado, codigo)
        "update EstoqueBro set modifica = '{}'".format(data)
        con.execute(sql)
        db_connection.commit()
        print("Estoque atualizado com sucesso! Data de Modificação:", data)


    except Exception as erro:
        print(erro)