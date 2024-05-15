import flet as ft
from flet import border
from flet import colors
from decimal import Decimal
#Definir botoes
botoes = [
    {'operador':'tan','font':'#ffffff','fundo':'#575a5e','largura':60,'altura':50},
    {'operador': 'sin', 'font': '#ffffff', 'fundo': '#575a5e','largura':60,'altura':50},
    {'operador': 'cos', 'font': '#ffffff', 'fundo': '#575a5e','largura':60,'altura':50},
    {'operador': 'sqrt', 'font': '#ffffff', 'fundo': '#575a5e','largura':60,'altura':50},
    {'operador': 'log', 'font': '#ffffff', 'fundo': '#575a5e','largura':60,'altura':50},
    {'operador': 'log10', 'font': '#ffffff', 'fundo': '#575a5e','largura':60,'altura':50},
    {'operador': 'e', 'font': '#ffffff', 'fundo': '#575a5e','largura':60,'altura':50},
    {'operador': 'pow', 'font': '#ffffff', 'fundo': '#575a5e','largura':60,'altura':50},
    {'operador': 'rad', 'font': '#ffffff', 'fundo': '#575a5e','largura':60,'altura':50},
    {'operador': 'pi', 'font': '#ffffff', 'fundo': '#575a5e','largura':60,'altura':50},
    {'operador': '(', 'font': '#ffffff', 'fundo': '#575a5e','largura':60,'altura':50},
    {'operador': ')', 'font': '#ffffff', 'fundo': '#575a5e','largura':60,'altura':50},

    {'operador': 'AC ', 'font': '#000000', 'fundo': '#f9d12c','largura':131,'altura':50},
    {'operador': '% ', 'font': '#000000', 'fundo': '#f9d12c','largura':60,'altura':50},
    {'operador': '/ ', 'font': '#000000', 'fundo': '#f9d12c','largura':60,'altura':50},

    {'operador': '7', 'font': '#f9d12c', 'fundo': '#000000','largura':60,'altura':50},
    {'operador': '8', 'font': '#f9d12c', 'fundo': '#000000','largura':60,'altura':50},
    {'operador': '9', 'font': '#f9d12c', 'fundo': '#000000','largura':60,'altura':50},

    {'operador': '* ', 'font': '#000000', 'fundo': '#f9d12c', 'largura': 60, 'altura': 50},

    {'operador': '4', 'font': '#f9d12c', 'fundo': '#000000','largura':60,'altura':50},
    {'operador': '5', 'font': '#f9d12c', 'fundo': '#000000','largura':60,'altura':50},
    {'operador': '6', 'font': '#f9d12c', 'fundo': '#000000','largura':60,'altura':50},

    {'operador': '- ', 'font': '#000000', 'fundo': '#f9d12c', 'largura': 60, 'altura': 50},

    {'operador': '1', 'font': '#f9d12c', 'fundo': '#000000','largura':60,'altura':50},
    {'operador': '2', 'font': '#f9d12c', 'fundo': '#000000','largura':60,'altura':50},
    {'operador': '3', 'font': '#f9d12c', 'fundo': '#000000','largura':60,'altura':50},

    {'operador': '+ ', 'font': '#000000', 'fundo': '#f9d12c', 'largura': 60, 'altura': 50},

    {'operador': '0', 'font': '#f9d12c', 'fundo': '#000000','largura':131,'altura':50},
    {'operador': '.', 'font': '#f9d12c', 'fundo': '#000000','largura':60,'altura':50},

    {'operador': '= ', 'font': '#000000', 'fundo': '#f9d12c', 'largura': 60, 'altura': 50},
]


#Adicionar borda:
borda_superior = border.BorderSide(1, 'white')  # Borda superior preta de 1 pixel
borda_inferior = border.BorderSide(1, 'white')  # Borda inferior preta de 1 pixel
borda_lateral = border.BorderSide(1, 'white')   # Borda lateral preta de 1 pixel

# Instância para borda
borda = border.Border(top=borda_superior, bottom=borda_inferior, left=borda_lateral, right=borda_lateral)
def pagina(page: ft.Page): #Criar pagina
    page.bgcolor = colors.BLACK
    page.window_resizable = True #Permitir mobilidade
    page.window_width = 330  # Largura
    page.window_height = 660  # Altura
    page.title = 'Calculadora Científica'  # Título
    page.window_always_on_top = True  # Janela sempre visível

    resultados = ft.Text(value='0',color=colors.WHITE,size=20) #Definindo o resultado


    display = ft.Row(  # Organizar uma linha
        width=250,
        height=100,
        controls=[resultados],
        alignment='end'
    )



    #Criando os botoes
    botao = [ft.Container(
        content=ft.Text(value=botao['operador'], color=botao['font']),
        width= botao['largura'],
        height= botao['altura'],
        bgcolor=botao['fundo'],
        border_radius=10, #Aredondar
        border= borda,  # Borda
        alignment=ft.alignment.center,
        #on_click=select  # Chamar função select
        margin= 0
    ) for botao in botoes]

    keybord = ft.Row(
        width=280,
        wrap=True,  # Quebrar linha
        controls=botao,
        alignment='end'
    )

    page.add(display,keybord)  # Adicionado o resultado

ft.app(target=pagina) #Executar