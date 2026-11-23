from src.model.despesa_model import Despesa

import flet as ft

class VisualizarDespesaView(ft.View):
    def __init__(self, pagina:ft.Page):
        super().__init__()

        self.pagina = pagina

        self.route = "/todasdespesas"

        self.title = ""
        self.bgcolor = "#fff9e4"
        self.horizontal_alignment = "center"
        self.vertical_alignment = "center"
        self.height = 800 #altura da janela
        self.width = 1000 # largura da janela

        dados_usuario = pagina.session.store.get("usuario_logado")
        self.id_usuario = dados_usuario.get("id_usuario")

        titulo = ft.Text(value = "Visualize suas despesas",
                        size=30,
                        color="#5c321f",
                        font_family="Georgia",
                        text_align="center")
        
        lista_despesas = []
        
        tabela = ft.DataTable(columns=[ft.DataColumn(label="ID DA CATEGORIA"),
                                       ft.DataColumn(label="DESCRIÇÃO"),
                                       ft.DataColumn(label="CATEGORIA"),
                                       ft.DataColumn(label="VALOR"),
                                       ft.DataColumn(label="DATA")],
                                       rows=lista_despesas)
        

        self.controls =[titulo,
                        tabela]


        
    



