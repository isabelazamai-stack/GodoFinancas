from src.database.conexao import Conexao

objeto_conexao = Conexao()
conexao, cursor = objeto_conexao.conectar()
print(conexao)