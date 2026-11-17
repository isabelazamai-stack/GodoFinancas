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
                             color="#5c321f",
                             font_family="Georgia",
                             size=30)

        self.botao_adicionar = ft.Button(content = "Adicionar",
                                width= 140,
                                height= 45,
                                color= "#000000",
                                bgcolor= "#cc9b85",
                                on_click = self.cadastrar_categoria)

        self.nome_cat = ft.TextField(label = "Nome da Categoria",
                                    bgcolor="#cc9b85",
                                    color="#000000",
                                    )


        self.lista_categorias = []
        coluna_lista_categorias = ft.Column(controls=self.lista_categorias)
        titulo_lista = ft.Text(value="CATEGORIAS CADASTRADAS")
        self.atualizar_lista_categoria()
        

        self.controls =[self.title,
                        self.nome_cat,
                        self.botao_adicionar,
                        titulo_lista,
                        coluna_lista_categorias]

    def cadastrar_categoria(self):
        nome_categoria = self.nome_cat.value
        resultado = Categoria().adicionar(nome_categoria, self.id_usuario)

        if resultado:
            self.pagina.show_dialog(ft.SnackBar(ft.Text("Categoria Cadastrada com sucesso!"),
                                                        bgcolor="#9fb67b"))
            self.lista_categorias.clear()
        else:
            self.pagina.show_dialog(ft.SnackBar(ft.Text("Cadastro Categoria não efetuada!"),
                                                        bgcolor = "#ff9191"))
        self.atualizar_lista_categoria()
            

    def atualizar_lista_categoria(self):
        categorias = Categoria().recuperar_todos(self.id_usuario)

        for categoria in categorias:
            nome_categoria = categoria.get("nome")
            texto = ft.Text(value = nome_categoria)
            self.lista_categorias.append(texto)
        self.pagina.update()