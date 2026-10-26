from src.database.conexao import Conexao

class Despesa:
    def __init__(self):
        pass

    @staticmethod
    def incluir (id_categoria: int, descricao: str, valor: int, data:str ) -> int:
        conexao, cursor = Conexao().conectar()

        if not conexao:
            print("Erro ao conectar!")
            return None

        try:
            cursor.execute("""
                        INSERT INTO tb_despesas (id_categoria, descricao, valor, data_despesa)
                        VALUES (%s, %s, %s, %s)
                        """,
                        [id_categoria,descricao,valor, data])
        
            conexao.commit()
            conexao.close()
            return True

        except Exception as e:
            print(f"Erro em incluir: {e}")
            return False

