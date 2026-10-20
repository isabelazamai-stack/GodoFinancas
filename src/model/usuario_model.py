from src.database.conexao import Conexao
class Usuario:
    def __init__(self):
        pass

    @staticmethod
    def cadastrar(login:str, senha:str) -> bool:
        conex, cur = Conexao().conectar()

        if not conex:
            print("Erro ao tentar conectar!")
            return False

        try:
            cur.execute("""
                        INSERT INTO tb_usuarios(usuario, senha)
                        VALUES (%s, %s)
                        """,
                        [login, senha])

            conex.commit()
            conex.close()

            return True
        
        except Exception as e:
            print(f"ERRO AO INSERIR:{e}")
            return False

    @staticmethod
    def verificar(login:str, senha=str) -> dict:
        conex, cur = Conexao().conectar()

        if not conex:
            print("Login e senha verificado")
            return {}

        
        cur.execute("""
                    select * from tb_usuarios
                    where usuario = %s
                    and senha = %s
                    """,
                    [login, senha])

        cur.fetchone()

        

        

