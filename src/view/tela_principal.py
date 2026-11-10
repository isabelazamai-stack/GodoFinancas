import flet as ft

class TelaPrincipal(ft.View):
    def __init__(self, pagina:ft.Page):
        super().__init__()

        self.pagina = pagina

        self.route = "/telaprincipal"

        dados_usuario = pagina.session.get("usuario_logado")
        nome_usuario = dados_usuario.get("usuario")

        self.title = ""
        self.bgcolor = "#67ffd9"
        self.horizontal_alignment = "center"
        self.vertical_alignment = "center"
        self.height = 800 #altura da janela
        self.width = 1000 # largura da janela

        titulo = ft.Text(value = f"Seja Bem-Vindo(a) {nome_usuario}",
                        size=30,
                        color="#000000",
                        font_family="Georgia")

        self.controls =[titulo
                        ]