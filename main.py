import flet as ft
from src.view.cadastro_usuario_view import CadastroUsuarioView
from src.view.login_usuario_view import LoginUsuarioView
from src.view.tela_principal import TelaPrincipal
from src.view.cadastro_categoria import CadastroCategoriaView
from src.view.add_despesa import AdicionarDespesaView
from src.view.todas_despesas import VisualizarDespesaView


def main(pagina:ft.Page):

    def navegacao(componente):
        item_clicado = componente.control.selected_index
        if item_clicado == 0:
            pagina.navigate("/cadastrocategoria")
        elif item_clicado == 1:
            pagina.navigate("/despesa")
        elif item_clicado == 2:
            pagina.navigate("/todasdespesas")
        elif item_clicado == 3:
            pagina.navigate("/")
        elif item_clicado == 4:
            pagina.navigate("/login")
    barra_navegacao = ft.NavigationBar(destinations=[
            ft.NavigationBarDestination(icon=ft.Icons.CATEGORY, label="Categoria"),
            ft.NavigationBarDestination(icon=ft.Icons.ADD_CIRCLE, label="Adicionar Despesa"),
            ft.NavigationBarDestination(icon=ft.Icons.WALLET_OUTLINED, label="Todas as Despesas"),
            ft.NavigationBarDestination(ft.Icons.EVENT_NOTE_OUTLINED, label="Despesa por Categoria"),
            ft.NavigationBarDestination(ft.Icons.ARROW_FORWARD_ROUNDED, label="Sair")],
            on_change=navegacao)


    tela_cadastro_usuario = CadastroUsuarioView(pagina)
    tela_login_usuario = LoginUsuarioView(pagina)
    cadastro_categoria = CadastroCategoriaView(pagina)
    cadastro_categoria.navigation_bar = barra_navegacao
    adicionar_despesa = AdicionarDespesaView(pagina)
    adicionar_despesa.navigation_bar = barra_navegacao
    visualizar_despesas = VisualizarDespesaView(pagina)
    visualizar_despesas.navigation_bar = barra_navegacao
    tela_principal = TelaPrincipal(pagina)
    tela_principal.navigation_bar = barra_navegacao


    #criando a função que fará o roteamento das páginas
    def roteamento(e=None):
        pagina.views.clear()

        if pagina.route == "/cadastro":
            pagina.views.append(tela_cadastro_usuario)

        elif pagina.route == "/login":
            pagina.views.append(tela_login_usuario)

        elif pagina.route == "/telaprincipal":
                    pagina.views.append(tela_principal)

        elif pagina.route == "/cadastrocategoria":
            pagina.views.append(cadastro_categoria)

        elif pagina.route == "/despesa":
                pagina.views.append(adicionar_despesa)

        elif pagina.route == "/todasdespesas":
                pagina.views.append(visualizar_despesas)

        pagina.update()

    #Associando a função de roteamento para sempre que houver uma troca de tela, esta função será chamada
    pagina.on_route_change = roteamento
    roteamento()

    #Abrindo a página incial
    pagina.views.append(tela_principal)

ft.run(main)