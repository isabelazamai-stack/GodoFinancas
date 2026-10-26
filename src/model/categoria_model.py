from src.database.conexao import Conexao

class Categoria:
    def __init__(self):
        pass

    @staticmethod
    def adicionar (nome_categoria:str, id_usuario: int) -> int:
        conexao, cursor = Conexao().conectar()

        if not conexao:
            print("Erro ao conectar!")
            return None
        try:
            cursor.execute("""
                        INSERT INTO tb_categoria(nome, id_usuario)
                        VALUES (%s, %s)
                        """,
                        [nome_categoria, id_usuario])
            
            id_categoria = cursor.lastrowid
            
            conexao.commit()
            conexao.close()
            return id_categoria
        
        except Exception as e:
            print(f"Errro em cadastrar: {e}")
            return False
        


    @staticmethod
    def excluir (id_categoria: int) -> bool:
        conexao, cursor = Conexao().conectar()

        if not conexao:
            print("Erro ao conectar!")
            return None
        
        try:
            cursor.execute("""
                            DELETE FROM tb_categoria
                            WHERE id_categoria = %s
                            """,
                            [id_categoria])
        

            conexao.commit()
            conexao.close()
            return True

        except Exception as e:
            print(f"ERRO AO ADICIONAR:{e}")
            return None
        


    #recuperar todos
    @staticmethod
    def recuperar_todos (categoria: int, login:str) -> dict:
        conexao, cursor = Conexao().conectar()

        if not conexao:
            print("Erro ao conectar!")
            return False
        try:
            cursor.execute("""
                            INSERT INTO tb_categoria(id_categoria, login)
                            VALUES (%s, %s)
                            """,
                            [categoria, login])
            conexao.commit()
            conexao.close()
            return True

        except Exception as e:
            print(f"ERRO AO ADICIONAR:{e}")
            return False
        
