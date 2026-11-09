import flet as ft
from src.model.usuario_model import Usuario


class CadastroUsuarioView(ft.View):
    def __init__(self, pagina:ft.Page):
        super().__init__()

        self.pagina = pagina


        self.title = ""
        self.bgcolor = "#FFF6C0"
        self.horizontal_alignment = "center"
        self.vertical_alignment = "center"
        self.height = 800 #altura da janela
        self.width = 1000 # largura da janela


        titulo = ft.Text(value = "CRIAR NOVA CONTA",
                          size=30,
                          color="#000000",
                          font_family="Georgia")


        subtitulo = ft.Text(value = "PREENCHA OS DADOS ABAIXO",
                            size=15,
                            color="#000000",
                            font_family="Times New Roman")


        self.campo_usuario = ft.TextField(label = "Usuário:",
                                        bgcolor = "#fcc2cf",
                                        border_color= "#ff92ad",
                                        border_width= 3,
                                        value = "")


        self.campo_senha = ft.TextField(label = "Senha:",
                                        password = True,
                                        can_reveal_password = True,
                                        bgcolor = "#fcc2cf",
                                        border_color= "#ff92ad",
                                        border_width= 3,
                                        value = "")


        botao_cadastrar = ft.Button(content = "Cadastrar-se",
                        width= 140,
                        height= 45,
                        color= "#000000",
                        bgcolor= "#FFE59D",
                        on_click = self.cadastrar
                        )


        botao_entrar = ft.Button(content = "Entrar",
                                width= 140,
                                height= 45,
                                color= "#000000",
                                bgcolor= "#FFE59D",
                                )
        
        linha = ft.Row(controls=[botao_cadastrar,
                                botao_entrar,],
                                alignment="center",
                                spacing=20)


        self.controls =[titulo,
                        subtitulo,
                        self.campo_usuario,
                        self.campo_senha,
                        linha]

  
    def cadastrar(self):
        usuario = self.campo_usuario.value
        senha = self.campo_senha.value
      
        resultado = Usuario().cadastrar(usuario , senha)

        if resultado == True:
            self.pagina.show_dialog(ft.SnackBar(ft.Text("Cadastro efetuado com sucesso"), bgcolor="#ff96ad"))
            #snackBar que deu certo

        else:
            pass
            #snackBar que deu errado
            

        