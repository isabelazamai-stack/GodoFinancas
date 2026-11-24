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

        dados_usuario = pagina.session.store.get("usuario_logado")
        self.id_usuario = dados_usuario.get("id_usuario")

        titulo = ft.Text(value = "Visualize suas despesas",
                        size=30,
                        color="#5c321f",
                        font_family="Georgia")
        
        self.lista_despesas = []
        
        tabela = ft.DataTable(columns=[ft.DataColumn(label="ID DA CATEGORIA"),
                                       ft.DataColumn(label="DESCRIÇÃO"),
                                       ft.DataColumn(label="CATEGORIA"),
                                       ft.DataColumn(label="VALOR"),
                                       ft.DataColumn(label="DATA")],
                                       rows=self.lista_despesas)

        self.atualizar_lista_despesas()
        

        self.controls =[titulo,
                        tabela]

    def atualizar_lista_despesas(self):
        despesas = Despesa().recuperar_todos(self.id_usuario)

        for despesa in despesas:
            id_despesa = str(despesa.get("id_despesa"))
            descricao = str(despesa.get("descricao"))
            valor = str(despesa.get("valor"))
            id_categoria = str(despesa.get("id_categoria"))
            data = str(despesa.get("data_despesa"))
        
            linha = ft.DataRow(
                color="#fff0f0",
                cells=[ft.DataCell(ft.Text(id_despesa)),
                                     ft.DataCell(ft.Text(descricao)),
                                     ft.DataCell(ft.Text(valor)),
                                     ft.DataCell(ft.Text(id_categoria)),
                                     ft.DataCell(ft.Text(data)),])

            self.lista_despesas.append(linha)

        self.pagina.update()




        
    



