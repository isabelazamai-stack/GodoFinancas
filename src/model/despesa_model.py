from src.database.conexao import Conexao

class Despesa:
    def __init__(self):
        pass

    @staticmethod
    def incluir (id_usuario:int, id_categoria: int, descricao: str, valor: float, data:str ) -> int:
        conexao, cursor = Conexao().conectar()

        if not conexao:
            print("Erro ao conectar!")
            return None

        try:
            cursor.execute("""
                        INSERT INTO tb_despesas (id_usuario, valor, data_despesa, descricao, id_categoria)
                        VALUES (%s, %s, %s, %s, %s)
                        """,
                        [id_usuario, valor, data, descricao, id_categoria ])

            id_despesa = cursor.lastrowid
        
            conexao.commit()
            conexao.close()
            return id_despesa

        except Exception as e:
            print(f"Erro em incluir: {e}")
            return False

    @staticmethod
    def recuperar_todos (login: str)-> list:
        conexao, cursor = Conexao().conectar()

        if not conexao:
            print("Erro ao conectar!")
            return None
        try:
            cursor.execute("""
                            SELECT id_usuario, valor, data_despesa, descricao, id_categoria
                            FROM tb_despesas
                            WHERE id_usuario = %s
                            """,
                            [login])
                
            despesa_recuperar = cursor.fetchall()
            conexao.close()
            return despesa_recuperar
        
        except Exception as e:
            print(f"Erro ao excluir: {e}")
            return None

    @staticmethod
    def recuperar_por_categoria (id_usuario: int, id_categoria: int)->list:
        conexao, cursor = Conexao().conectar()
        
        if not conexao:
            print("Erro ao conectar!")
            return None
        try:
            cursor.execute("""
                            SELECT id_usuario, valor, data_despesa, descricao, id_categoria
                            FROM tb_despesas
                            WHERE id_usuario = %s
                            AND id_categoria = %s
                            """,
                            [id_usuario, id_categoria])
                
            despesa_recuperar = cursor.fetchall()
            conexao.close()
            return despesa_recuperar
        
        except Exception as e:
            print(f"Erro ao excluir: {e}")
            return None

    @staticmethod
    def excluir (id_despesa: int) -> bool:
            conexao, cursor = Conexao().conectar()
    
            if not conexao:
                print("Erro ao conectar!")
                return None
            
            try:
                cursor.execute("""
                                DELETE FROM tb_despesas
                                WHERE id_despesa = %s
                                """,
                                [id_despesa])
            
    
                conexao.commit()
                conexao.close()
                return True
    
            except Exception as e:
                print(f"ERRO AO EXCLUIR:{e}")
                return False

    @staticmethod
    def alterar (id_despesa: int, id_usuario: int, id_categoria:int, descricao: str, valor: float, data: str) -> bool:
        conexao, cursor = Conexao().conectar()
        if not conexao:
            print("Erro ao conectar!")
            return False
                    
        try:
            cursor.execute("""
                            UPDATE tb_despesas SET
                                    id_categoria = %s, 
                                    descricao = %s, 
                                    valor=%s, 
                                    data_despesa=%s 
                            WHERE id_despesa = %s
                            AND id_usuario = %s;
                            """,
                            [id_categoria, descricao, valor, data, id_despesa, id_usuario])
        
            conexao.commit()
            conexao.close()
            return True

        except Exception as e:
            print(f"ERRO AO EXCLUIR:{e}")
            return False



