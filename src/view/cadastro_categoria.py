import flet as ft
from src.model.categoria_model import Categoria


class CadastroCategoriaView(ft.View):
    def __init__(self, pagina:ft.Page):
        super().__init__()

        self.pagina = pagina

        self.route = "/cadastrocategoria"

        self.title = ft.Text(value="Cadastre as Categoria",
                             color="#000000",
                             horizontal_alignment = "center",
                             font_family="Georgia",
                             size=30,)

        self.campo_usuario = ft.TextField(label = "Categorias:",
                                                bgcolor = "#dbe7e4",
                                                border_color= "#c5dedc",
                                                border_width= 3,
                                                value = "")

        self.botao_adicionar = ft.Button(content = "Adicionar",
                                width= 140,
                                height= 45,
                                color= "#000000",
                                bgcolor= "#fad2e1"
                                )
        
        self.height = 800 #altura da janela
        self.width = 1000 # largura da janela

        self.controls =[self.title,
                        self.campo_usuario,
                        self.botao_adicionar]

    # def adicionar(self):
        