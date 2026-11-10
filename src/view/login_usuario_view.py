import flet as ft
from src.model.usuario_model import Usuario


class LoginUsuarioView(ft.View):
    def __init__(self, pagina:ft.Page):
        super().__init__()

        self.pagina = pagina

        self.route = "/login"

        self.title = ""
        self.bgcolor = "#fde2e4"
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
                                        bgcolor = "#dbe7e4",
                                        border_color= "#c5dedc",
                                        border_width= 3,
                                        value = "")


        self.campo_senha = ft.TextField(label = "Senha:",
                                        password = True,
                                        can_reveal_password = True,
                                        bgcolor = "#dbe7e4",
                                        border_color= "#c5dedc",
                                        border_width= 3,
                                        value = "")

        
        botao_entrar = ft.Button(content = "Entrar",
                        width= 140,
                        height= 45,
                        color= "#000000",
                        bgcolor= "#fad2e1",
                        on_click=self.ir_para_login
                        )

        nao_tem_conta = ft.Text(value = "Não tem uma conta?",
                                            size=20,
                                            color="#000000",
                                            font_family="Times New Roman")

        botao_cadastrar = ft.Button(content = "Cadastar-se",
                                width= 140,
                                height= 45,
                                color= "#000000",
                                bgcolor= "#fad2e1",
                                on_click=self.ir_para_cadastrar
                                )


        self.controls =[titulo,
                        subtitulo,
                        self.campo_usuario,
                        self.campo_senha,
                        botao_entrar,
                        nao_tem_conta,
                        botao_cadastrar,
                        ]

    async def ir_para_cadastrar(self):
        await self.pagina.push_route("/cadastro")

    def ir_para_login(self):
        usuario = self.campo_usuario.value
        senha = self.campo_senha.value
        
        resultado = Usuario().verificar(usuario , senha)

        if resultado:
            self.pagina.show_dialog(ft.SnackBar(ft.Text("Login efetuado com sucesso"), bgcolor="#9fb67b"))
            self.pagina.session.store.set("usuario_logado",resultado)
            self.pagina.navigate("/cadastrocategoria")

        else:
            self.pagina.show_dialog(ft.SnackBar(ft.Text("Login não efetuado. Tente novamente"), bgcolor="#ff9191"))

    

    