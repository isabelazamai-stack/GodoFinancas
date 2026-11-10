import flet as ft
from src.model.usuario_model import Usuario


class PaginaUsuarioView(ft.View):
    def __init__(self, pagina:ft.Page):
        super().__init__()

        self.pagina = pagina

        self.route = "/login"

        self.title = ""
        self.bgcolor = "#dbe7e4"
        self.horizontal_alignment = "center"
        self.vertical_alignment = "center"
        self.height = 800 #altura da janela
        self.width = 1000 # largura da janela

        titulo = ft.Text(value = "Tela Principal",
                        size=30,
                        color="#000000",
                        font_family="Georgia")
        
        subtitulo = ft.Text(value = "Você está logado",
                            size=20,
                            color="#000000",
                            font_family="Times New Roman")

        self.controls =[titulo,
                        subtitulo
                        ]