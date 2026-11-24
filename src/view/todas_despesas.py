from src.model.despesa_model import Despesa
import flet as ft

class VisualizarDespesaView(ft.View):
    def __init__(self, pagina:ft.Page):
        super().__init__()

        self.pagina = pagina

        self.route = "/todasdespesas"

        self.title = ""
        self.bgcolor = "#fff9e4"

        dados_usuario = pagina.session.store.get("usuario_logado")
        self.id_usuario = dados_usuario.get("id_usuario")

        titulo = ft.Text(value = "Visualize suas despesas",
                        size=30,
                        color="#5c321f",
                        font_family="Georgia")
        
        self.lista_despesas = []
        
                                       
        tabela = ft.DataTable(columns=[ft.DataColumn(label="ID DA CATEGORIA"),
                                       ft.DataColumn(label="ID DA DESPESA"),
                                       ft.DataColumn(label="DESCRIÇÃO"),
                                       ft.DataColumn(label="VALOR"),
                                       ft.DataColumn(label="DATA"),
                                       ft.DataColumn(label="CATEGORIA"),
                                       ft.DataColumn(label="EXCLUIR")],
                                       rows=self.lista_despesas)

        self.atualizar_lista_despesas()
        

        self.controls =[titulo,
                        tabela]

    def atualizar_lista_despesas(self):
        self.lista_despesas.clear()
        
        despesas = Despesa().recuperar_todos(self.id_usuario)

        for despesa in despesas:
            id_categoria = str(despesa.get("id_categoria"))
            id_despesa = str(despesa.get("id_despesa"))
            descricao = str(despesa.get("descricao"))
            valor = str(despesa.get("valor"))
            data = str(despesa.get("data_despesa"))
            nome= str(despesa.get("nome"))
        
            linha = ft.DataRow(
                color="#fff0f0",
                            cells=[ft.DataCell(ft.Text( id_categoria)),
                                     ft.DataCell(ft.Text(id_despesa)),
                                     ft.DataCell(ft.Text(descricao)),
                                     ft.DataCell(ft.Text(valor)),
                                     ft.DataCell(ft.Text(data)),
                                     ft.DataCell(ft.Text(nome)),
                                     ft.DataCell(ft.IconButton(icon=ft.Icons.DELETE,
                                                               key=id_despesa,
                                                               on_click = self.excluir_despesa))])

            self.lista_despesas.append(linha)
        self.pagina.update()

    def excluir_despesa(self, botao):
        id_despesa = botao.control.key
        Despesa().excluir(id_despesa)
        self.atualizar_lista_despesas()
        




        
    



