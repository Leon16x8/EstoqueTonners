import mysql.connector #acessa o SQL
from mysql.connector import errorcode #trata as "exceções" (erros)

def conectar():
    try:
        db_connection = mysql.connector.connect(host='192.168.15.107',user='LeonardoTI',password='Novaadm@2463',database='BDEstoque', consume_results = True)
        print('Conectado com sucesso')

        return db_connection
    except mysql.connector.Error as erro: #Guardando as possiveis exceções na variável
        if erro.errno == errorcode.ER_BAD_DB_ERROR: #caso o banco de dados não exista
            print('Banco de Dados não existe!, {}'.format(erro))
        elif erro.errno == errorcode.ER_ACCESS_DENIED_ERROR: #Caso usuário ou senha estejam errados
            print('Usuário ou Senha não são válidos, {}'.format(erro))
        else:
            print(erro)
    else:
        db_connection.close()