from src.database.conexao import Conexao
class Categoria:
    def __init__(self):
        pass

    @staticmethod:
    def adicionar (categoria:int) -> bool:
        conexao, cursor = Conexao().conectar()

        if not conexao:
            print("Erro ao conectar")
            return False
        try:
            cursor.execute("""
                        INSERT INTO tb_categoria(categoria)
                        VALUES (%s)
                        """,
                        [categoria])
            conexao.commit()
            conexao.close()
            return True
        except Exception as e:
            print(f"ERRO AO ADICIONAR:{e}")
            return False


    #recuperar todos
    @staticmethod
    def recuperar_todos (categoria: int, login:str) -> dict:
        conexao, cursor = conexao().conectar()

        if not conexao:
            print("Erro ao conectar!")
            return False
        try:
            cursor.execute("""
                            INSERT INTO tb_categoria(categoria, login)
                            VALUES (%s, %s)
                            """,
                            [categoria, login])
            conexao.commit()
            conexao.close()
            return True

        except Exception as e:
            print(f"ERRO AO ADICIONAR:{e}")
            return False

    @staticmethod
    def excluir (id_categoria: int) -> bool:
        conexao, cursor = conexao().conectar()

        if not conexao:
            print("Erro ao conectar!")
            return False
        try:
            cursor.execute("""
                            INSERT INTO tb_categoria(id_categoria)
                            VALUES (%s)
                            """,
                            [id_categoria])
            conexao.commit()
            conexao.close()
            return True

        except Exception as e:
            print(f"ERRO AO ADICIONAR:{e}")
            return False
        
