from src.model.categoria_model import Categoria
from src.model.despesa_model import Despesa
import flet as ft

class AdicionarDespesaView(ft.View):
    def __init__(self, pagina:ft.Page):
        super().__init__()

        self.pagina = pagina

        self.route = "/adicionardespesa"

        self.title = ""
        self.bgcolor = "#fff9e4"
        self.horizontal_alignment = "center"
        self.vertical_alignment = "center"
        self.height = 800 #altura da janela
        self.width = 1000 # largura da janela

        dados_usuario = pagina.session.store.get("usuario_logado")
        self.id_usuario = dados_usuario.get("id_usuario")

        titulo = ft.Text(value = "Adicione suas despesas",
                        size=30,
                        color="#5c321f",
                        font_family="Georgia")
        
        campo_descricao = ft.TextField(label="Descrição")

        campo_valor = ft.TextField(label="Valor",
                                   keyboard_type=ft.KeyboardType.NUMBER)
        
        campo_data = ft.TextField(label="Data",
                                  keyboard_type=ft.KeyboardType.DATETIME)
        

        categorias = Categoria().recuperar_todos(self.id_usuario)

        opcoes = []

        for categoria in categorias:
            opcoes.append(ft.DropdownOption(key=categoria.get("id-categoria"),
                                            text=categoria.get("nome")))

        campo_categoria = ft.Dropdown(options=opcoes)

        botao_adicionar = ft.Button(content="Cadastrar")


        self.controls =[titulo,
                        campo_descricao,
                        campo_valor,
                        campo_data,
                        campo_categoria,
                        botao_adicionar]
        
         

    


