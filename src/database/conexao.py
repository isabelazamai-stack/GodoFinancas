import mysql.connector

class Conexao:
    def __init__(self):
        pass

    def conectar(self) -> list:
        #Conectando ao banco de dados
        conexao = mysql.connector.connect(host="127.0.0.1",
                                          port="3306",
                                          user= "root",
                                          password="root",
                                          database="bd_godofinancas")
        cursor = conexao.cursor()
        return conexao, cursor

    