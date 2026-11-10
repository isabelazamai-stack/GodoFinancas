import flet as ft
from src.model.usuario_model import Usuario


class CadastroUsuarioView(ft.View):
    def __init__(self, pagina:ft.Page):
        super().__init__()

        self.pagina = pagina

        self.route = "/cadastro"


        self.title = ""
        self.bgcolor = "#fde2e4"
        self.horizontal_alignment = "center"
        self.vertical_alignment = "center"
        self.height = 800 #altura da janela
        self.width = 1000 # largura da janela


        titulo = ft.Text(value = "Criar nova conta",
                          size=30,
                          color="#000000",
                          font_family="Georgia")


        subtitulo = ft.Text(value = "Preencha os dados abaixo",
                            size=20,
                            color="#000000",
                            font_family="Times New Roman")


        self.campo_usuario = ft.TextField(label = "Usuário:",
                                        bgcolor = "#dbe7e4",
                                        border_color= "#c5dedc",
                                        border_width= 3,
                                        value = "")


        self.campo_senha = ft.TextField(label = "Senha:",
                                        password = True,
                                        can_reveal_password = True,
                                        bgcolor = "#dbe7e4",
                                        border_color= "##dbe7e4",
                                        border_width= 3,
                                        value = "")

        
        botao_cadastrar = ft.Button(content = "Cadastrar-se",
                        width= 140,
                        height= 45,
                        color= "#000000",
                        bgcolor= "#fad2e1",
                        on_click = self.cadastrar
                        )

        ja_tem_conta = ft.Text(value = "Já tem uma conta?",
                                            size=20,
                                            color="#000000",
                                            font_family="Times New Roman")


        botao_entrar = ft.Button(content = "Entrar",
                                width= 140,
                                height= 45,
                                color= "#000000",
                                bgcolor= "#fad2e1",
                                on_click=self.ir_pro_login,
                                )


        self.controls =[titulo,
                        subtitulo,
                        self.campo_usuario,
                        self.campo_senha,
                        botao_cadastrar,
                        ja_tem_conta,
                        botao_entrar,
                        ]

  
    def cadastrar(self):
        usuario = self.campo_usuario.value
        senha = self.campo_senha.value
      
        resultado = Usuario().cadastrar(usuario , senha)

        if resultado:
            self.pagina.show_dialog(ft.SnackBar(ft.Text("Cadastro efetuado com sucesso"), bgcolor="#9fb67b"))
            #snackBar que deu certo

        else:
            self.pagina.show_dialog(ft.SnackBar(ft.Text("Cadastro não efetuado"), bgcolor="#ff9191"))
            #snackBar que deu errado

    async def ir_pro_login(self):
        await self.pagina.push_route("/login")


