from src.model.categoria_model import Categoria
from src.model.despesa_model import Despesa
from datetime import datetime
import flet as ft

class AdicionarDespesaView(ft.View):
    def __init__(self, pagina:ft.Page):
        super().__init__()

        self.pagina = pagina

        self.route = "/adicionardespesa"

        self.title = ""
        self.bgcolor = "#fff9e4"
        self.horizontal_alignment = "center"
        self.vertical_alignment = "center"
        self.height = 800 #altura da janela
        self.width = 1000 # largura da janela

        dados_usuario = pagina.session.store.get("usuario_logado")
        self.id_usuario = dados_usuario.get("id_usuario")

        titulo = ft.Text(value = "Adicione suas despesas",
                        size=30,
                        color="#5c321f",
                        font_family="Georgia")
        
        self.campo_descricao = ft.TextField(label="Descrição",
                                            bgcolor="#ffe4d9")

        self.campo_valor = ft.TextField(label="Valor",
                                   keyboard_type=ft.KeyboardType.NUMBER,
                                   bgcolor="#ffe4d9")
        
        self.campo_data = ft.TextField(label="Data",
                                  keyboard_type=ft.KeyboardType.DATETIME,
                                  bgcolor="#ffe4d9")
        

        categorias = Categoria().recuperar_todos(self.id_usuario)

        opcoes = []

        for categoria in categorias:
            opcoes.append(ft.DropdownOption(key=categoria.get("id_categoria"),
                                            text=categoria.get("nome")))

        self.campo_categoria = ft.Dropdown(options=opcoes,
                                           bgcolor="#ffe4d9")

        botao_adicionar = ft.Button(content="Cadastrar",
                                    bgcolor="#ffe4d9",
                                    on_click=self.cadastrar_despesa)


        self.controls =[titulo,
                        self.campo_descricao,
                        self.campo_valor,
                        self.campo_data,
                        self.campo_categoria,
                        botao_adicionar]
        
    def cadastrar_despesa(self):
        #puxando os valores
        descricao = self.campo_descricao.value
        valor = self.campo_valor.value
        data = self.campo_data.value
        data_convertida = datetime.strptime(data, "%d/%m/%Y").date()
        categoria = int(self.campo_categoria.value)

        #enviando para banco de dados
        resultado = Despesa().incluir(self.id_usuario,categoria,descricao,valor,data_convertida)
        if resultado:
            self.pagina.show_dialog(ft.SnackBar(ft.Text("Categoria Cadastrada com sucesso!"),
                                                        bgcolor="#9fb67b"))
        else:
            self.pagina.show_dialog(ft.SnackBar(ft.Text("Cadastro Categoria não efetuada!"),
                                                        bgcolor = "#ff9191"))
        self.page.update()
        
        
    

        
         

    


