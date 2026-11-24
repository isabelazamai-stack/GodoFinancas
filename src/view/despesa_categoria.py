import flet as ft

class DespesaPorCategoria(ft.View):
    def __init__(self, pagina:ft.Page):
        super().__init__()

        self.pagina = pagina

        self.route = "/despesacategoria"

        self.title = ""
        self.bgcolor = "#fff9e4"

        titulo = ft.Text(value = "Despesas Por categoria",
                        size=30,
                        color="#5c321f",
                        font_family="Georgia")

        self.controls =[titulo]