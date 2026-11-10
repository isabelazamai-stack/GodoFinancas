import flet as ft
from src.view.cadastro_usuario_view import CadastroUsuarioView
from src.view.login_usuario_view import LoginUsuarioView
from src.view.pagina_principal import PaginaUsuarioView


def main(pagina:ft.Page):
    barra_navegacao = ft.NavigationBar(destinations=[
            ft.NavigationBarDestination(icon=ft.Icons.CIRCLE, label="Categoria"),
            ft.NavigationBarDestination(icon=ft.Icons.ADD, label="Adicionar Despesa"),
            ft.NavigationBarDestination(icon=ft.Icons.ADD_ALERT_ROUNDED, label="Todas as Despesas"),
            ft.NavigationBarDestination(icon=ft.Icons.SIGNAL_CELLULAR_ALT_SHARP, label="Despesa por Categoria")])


    tela_cadastro_usuario = CadastroUsuarioView(pagina)
    tela_login_usuario = LoginUsuarioView(pagina)
    tela_login_usuario.navigation_bar = barra_navegacao
    tela_principal_usuario = PaginaUsuarioView(pagina)


    #criando a função que fará o roteamento das páginas
    def roteamento(e=None):
        pagina.views.clear()

        if pagina.route == "/cadastro":
            pagina.views.append(tela_cadastro_usuario)

        elif pagina.route == "/login":
            pagina.views.append(tela_login_usuario)

        elif pagina.route == "/cadastrocategoria":
            pagina.views.append(tela_principal_usuario)

        pagina.update()

    #Associando a função de roteamento para sempre que houver uma troca de tela, esta função será chamada
    pagina.on_route_change = roteamento
    roteamento()

    #Abrindo a página incial
    pagina.views.append(tela_login_usuario)

ft.run(main)