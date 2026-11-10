import flet as ft

class VisualizarDespesaView(ft.View):
    def __init__(self, pagina:ft.Page):
        super().__init__()

        self.pagina = pagina

        self.route = "/todasdespesas"

        self.title = ""
        self.bgcolor = "#dbe7e4"
        self.horizontal_alignment = "center"
        self.vertical_alignment = "center"
        self.height = 800 #altura da janela
        self.width = 1000 # largura da janela

        titulo = ft.Text(value = "Visualize suas despesas",
                        size=30,
                        color="#000000",
                        font_family="Georgia")

        self.controls =[titulo
                        ]