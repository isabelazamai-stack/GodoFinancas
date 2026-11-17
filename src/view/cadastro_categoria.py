import flet as ft
from src.model.categoria_model import Categoria

class CadastroCategoriaView(ft.View):
    def __init__(self, pagina:ft.Page):
        super().__init__()
        
        self.height = 800 #altura da janela
        self.width = 1000 # largura da janela
        self.pagina = pagina
        self.bgcolor = "#fff9e4"
        self.route = "/cadastrocategoria"


        dados_usuario = pagina.session.store.get("usuario_logado")
        self.id_usuario = dados_usuario.get("id_usuario")

        self.title = ft.Text(value="Cadastre as Categoria",
                             color="#ff619b",
                             font_family="Georgia",
                             size=30)

        self.botao_adicionar = ft.Button(content = "Adicionar",
                                width= 140,
                                height= 45,
                                color= "#000000",
                                bgcolor= "#ff8ab5",
                                on_click = self.cadastrar_categoria)

        self.nome_cat = ft.TextField(label = "Nome da Categoria",
                                    bgcolor="#ffcbde",
                                    color="#000000",
                                    )

        self.historico = []
        self.coluna = ft.Column(controls = self.historico)

        self.controls =[self.title,
                        self.nome_cat,
                        self.botao_adicionar,
                        self.coluna]

    def cadastrar_categoria(self):
        nome_categoria = self.nome_cat.value
        resultado = Categoria().adicionar(nome_categoria, self.id_usuario)

        if resultado:
            self.page.show_dialog(ft.SnackBar(ft.Text("Categoria Cadastrada com sucesso!"),
                                                        bgcolor="#9fb67b"))
        else:
            self.page.show_dialog(ft.SnackBar(ft.Text("Cadastro Categoria não efetuada!"),
                                                        bgcolor = "#ff9191"))
            
            self.pagina.update()

        