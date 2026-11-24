from src.model.despesa_model import Despesa
from src.model.categoria_model import Categoria
import flet as ft

class DespesaPorCategoria(ft.View):
    def __init__(self, pagina:ft.Page):
        super().__init__()

        self.pagina = pagina

        self.route = "/despesacategoria"

        self.title = ""
        self.bgcolor = "#fff9e4"

        dados_usuario = pagina.session.store.get("usuario_logado")
        self.id_usuario = dados_usuario.get("id_usuario")
        

        titulo = ft.Text(value = "Despesas Por categoria",
                        size=30,
                        color="#5c321f",
                        font_family="Georgia")
        
        opcoes_categoria = []

        categorias = Categoria().recuperar_todos(self.id_usuario)

        for categoria in categorias:
            opcao = ft.DropdownOption(key=categoria.get("id_categoria"),
                                      text=categoria.get("nome"))
            opcoes_categoria.append(opcao)

        self.campo_categoria = ft.Dropdown(options= opcoes_categoria, on_select=self.atualizar_lista_despesas)

        self.lista_despesas = []
                                       
        tabela_despesas = ft.DataTable(columns=[ft.DataColumn(label="ID DA DESPESA"),
                                       ft.DataColumn(label="DESCRIÇÃO"),
                                       ft.DataColumn(label="VALOR"),
                                       ft.DataColumn(label="DATA"),
                                       ft.DataColumn(label="CATEGORIA"),
                                       ft.DataColumn(label="EXCLUIR")],
                                       rows=self.lista_despesas)

        self.atualizar_lista_despesas()
        

        self.controls =[titulo, self.campo_categoria, tabela_despesas]

    def atualizar_lista_despesas(self):
        self.lista_despesas.clear()
        id_categoria = self.campo_categoria.value
        
        despesas = Despesa().recuperar_por_categoria(self.id_usuario,id_categoria)

        for despesa in despesas:
            id_despesa = str(despesa.get("id_despesa"))
            descricao = str(despesa.get("descricao"))
            valor = str(despesa.get("valor"))
            data = str(despesa.get("data_despesa"))
            nome= str(despesa.get("nome"))
        
            linha = ft.DataRow(
                color="#fff0f0",
                            cells=[ft.DataCell(ft.Text(id_despesa)),
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
        




        
    



