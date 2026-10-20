import mysql.connector

class Conexao:
    def __init__(self):
        pass

    @staticmethod
    def conectar() -> list:

        try:
            #Conectando ao banco de dados
            conexao = mysql.connector.connect(host="127.0.0.1",
                                            port="3306",
                                            user= "root",
                                            password="root",
                                            database="bd_godofin")
            cursor = conexao.cursor()

            return conexao, cursor

        except Exception as e:
            print(f"ERRO: {e}")
            return None, None
