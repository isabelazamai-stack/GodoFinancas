import flet as ft
from src.model.usuario_model import Usuario


class LoginUsuarioView(ft.View):
    def __init__(self, pagina:ft.Page):
        super().__init__()

        self.pagina = pagina

        self.route = "/login"

        self.title = ""
        self.bgcolor = "#FFF6C0"
        self.horizontal_alignment = "center"
        self.vertical_alignment = "center"
        self.height = 800 #altura da janela
        self.width = 1000 # largura da janela


        titulo = ft.Text(value = "Entrar no Sistema",
                          size=30,
                          color="#000000",
                          font_family="Georgia")

        subtitulo = ft.Text(value = "Insira suas informações:",
                                    size=20,
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

        
        botao_entrar = ft.Button(content = "Entrar",
                        width= 140,
                        height= 45,
                        color= "#000000",
                        bgcolor= "#FFE59D",
                        on_click=self.logar
                        )

        nao_tem_conta = ft.Text(value = "Não tem uma conta?",
                                            size=20,
                                            color="#000000",
                                            font_family="Times New Roman")

        botao_cadastrar = ft.Button(content = "Cadastar-se",
                                width= 140,
                                height= 45,
                                color= "#000000",
                                bgcolor= "#FFE59D",
                                on_click=self.ir_pro_cadastrar
                                )


        self.controls =[titulo,
                        subtitulo,
                        self.campo_usuario,
                        self.campo_senha,
                        botao_entrar,
                        nao_tem_conta,
                        botao_cadastrar,
                        ]

    def logar(self):
        usuario = self.campo_usuario.value
        senha = self.campo_senha.value
        
        resultado = Usuario().verificar(usuario , senha)

        if resultado:
            self.pagina.show_dialog(ft.SnackBar(ft.Text("Login efetuado com sucesso"), bgcolor="#9fb67b"))
            #snackBar que deu certo

        else:
            self.pagina.show_dialog(ft.SnackBar(ft.Text("Login não efetuado. Tente novamente"), bgcolor="#ff9191"))
            #snackBar que deu errado

    
    async def ir_pro_cadastrar(self):
        await self.pagina.push_route("/cadastro")