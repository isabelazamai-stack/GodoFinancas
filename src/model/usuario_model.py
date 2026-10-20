from src.database.conexao import Conexao
class Usuario:
    def __init__(self):
        pass

    @staticmethod
    def cadastrar(login:str, senha:str) -> bool:

        conex, cur = Conexao().conectar()
        cur.execute("""
                    INSERT INTO tb_usuarios(usuario, senha)
                    VALUES (%s, %s)
                    """,
                    [login, senha])

        conex.commit()
        conex.close()
        return True

