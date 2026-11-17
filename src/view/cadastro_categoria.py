import flet as ft
from src.model.categoria_model import Categoria

class CadastroCategoriaView(ft.View):
    def __init__(self, pagina:ft.Page):
        super().__init__()
        
        self.height = 800 #altura da janela
        self.width = 1000 # largura da janela

        self.pagina = pagina
        self.bgcolor = "#dbe7e4"

        self.route = "/cadastrocategoria"

        self.title = ft.Text(value="Cadastre as Categoria",
                             color="#000000",
                             font_family="Georgia",
                             size=30)

        # self.campo = ft.Text(value = "Categorias:",
        #                              bgcolor = "#dbe7e4",
        #                              border_color= "#c5dedc",
        #                              border_width= 3)

        self.botao_adicionar = ft.Button(content = "Adicionar",
                                width= 140,
                                height= 45,
                                color= "#000000",
                                bgcolor= "#fad2e1",
                                on_click = self.incluir
                                )

        self.nome_cat = ft.TextField(label = "Nome da Categoria")

        self.historico = []
        self.coluna = ft.Column(controls = self.historico)
        

        self.controls =[self.title,
                        self.nome_cat,
                        self.botao_adicionar,
                        self.coluna]

    def incluir(self):
        dados_usuario = self.pagina.session.store.get("usuario_logado")
        nome_usuario = dados_usuario.get("login")
        categoria = self.nome_cat.value
        resultado = Categoria().adicionar(categoria,nome_usuario)
        if resultado:
            self.historico.append(ft.Text(value = f"{categoria}",
                                          color="#000000"))
            self.page.show_dialog(ft.SnackBar(ft.Text("Categoria Cadastrada com sucesso!"),
                                              bgcolor = "#ffffff"))
            self.pagina.update()

        