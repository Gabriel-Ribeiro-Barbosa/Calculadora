import flet as ft
from flet import border, colors
from decimal import Decimal
import math

# Definir botoes
botoes = [
    {'operador': 'tan', 'font': '#ffffff', 'fundo': '#575a5e', 'largura': 60, 'altura': 50},
    {'operador': 'sin', 'font': '#ffffff', 'fundo': '#575a5e', 'largura': 60, 'altura': 50},
    {'operador': 'cos', 'font': '#ffffff', 'fundo': '#575a5e', 'largura': 60, 'altura': 50},
    {'operador': 'sqrt', 'font': '#ffffff', 'fundo': '#575a5e', 'largura': 60, 'altura': 50},
    {'operador': 'log', 'font': '#ffffff', 'fundo': '#575a5e', 'largura': 60, 'altura': 50},
    {'operador': 'log10', 'font': '#ffffff', 'fundo': '#575a5e', 'largura': 60, 'altura': 50},
    {'operador': '(', 'font': '#ffffff', 'fundo': '#575a5e', 'largura': 60, 'altura': 50},
    {'operador': ')', 'font': '#ffffff', 'fundo': '#575a5e', 'largura': 60, 'altura': 50},
    {'operador': 'AC', 'font': '#000000', 'fundo': '#f9d12c', 'largura': 131, 'altura': 50},
    {'operador': '%', 'font': '#000000', 'fundo': '#f9d12c', 'largura': 60, 'altura': 50},
    {'operador': '/', 'font': '#000000', 'fundo': '#f9d12c', 'largura': 60, 'altura': 50},
    {'operador': '7', 'font': '#f9d12c', 'fundo': '#000000', 'largura': 60, 'altura': 50},
    {'operador': '8', 'font': '#f9d12c', 'fundo': '#000000', 'largura': 60, 'altura': 50},
    {'operador': '9', 'font': '#f9d12c', 'fundo': '#000000', 'largura': 60, 'altura': 50},
    {'operador': '*', 'font': '#000000', 'fundo': '#f9d12c', 'largura': 60, 'altura': 50},
    {'operador': '4', 'font': '#f9d12c', 'fundo': '#000000', 'largura': 60, 'altura': 50},
    {'operador': '5', 'font': '#f9d12c', 'fundo': '#000000', 'largura': 60, 'altura': 50},
    {'operador': '6', 'font': '#f9d12c', 'fundo': '#000000', 'largura': 60, 'altura': 50},
    {'operador': '-', 'font': '#000000', 'fundo': '#f9d12c', 'largura': 60, 'altura': 50},
    {'operador': '1', 'font': '#f9d12c', 'fundo': '#000000', 'largura': 60, 'altura': 50},
    {'operador': '2', 'font': '#f9d12c', 'fundo': '#000000', 'largura': 60, 'altura': 50},
    {'operador': '3', 'font': '#f9d12c', 'fundo': '#000000', 'largura': 60, 'altura': 50},
    {'operador': '+', 'font': '#000000', 'fundo': '#f9d12c', 'largura': 60, 'altura': 50},
    {'operador': '0', 'font': '#f9d12c', 'fundo': '#000000', 'largura': 131, 'altura': 50},
    {'operador': '.', 'font': '#f9d12c', 'fundo': '#000000', 'largura': 60, 'altura': 50},
    {'operador': '=', 'font': '#000000', 'fundo': '#f9d12c', 'largura': 60, 'altura': 50},
]

# Adicionar borda:
borda_superior = border.BorderSide(1, 'white')
borda_inferior = border.BorderSide(1, 'white')
borda_lateral = border.BorderSide(1, 'white')
borda = border.Border(top=borda_superior, bottom=borda_inferior, left=borda_lateral, right=borda_lateral)


# Função para avaliar a expressão
def avaliar_expressao(expr):
    try:
        result = eval(expr, {"__builtins__": None}, {
            'tan': math.tan,
            'sin': math.sin,
            'cos': math.cos,
            'sqrt': math.sqrt,
            'log': math.log,
            'log10': math.log10,
            'pi': math.pi,
            'e': math.e
        })
        return result
    except:
        return 'Error'


# Função de cálculo
def calcular(expr):
    try:
        result = avaliar_expressao(expr)
        if isinstance(result, float):
            digitos = min(abs(Decimal(result).as_tuple().exponent), 5)
            return format(result, f'.{digitos}f')
        return str(result)
    except:
        return 'Error'


# Função para selecionar e processar o evento
def select(event):
    valor_atual = resultados.value if resultados.value not in ('0', 'Error') else ''
    value = event.control.content.value

    if value.isdigit() or value == '.':
        value = valor_atual + value
    elif value == 'AC':
        value = '0'
    elif value == '=':
        value = calcular(valor_atual)
    else:
        value = valor_atual + value

    resultados.value = value
    resultados.update()


# Função para criar a página
def pagina(page: ft.Page):
    page.bgcolor = colors.BLACK
    page.window_resizable = True
    page.window_width = 330
    page.window_height = 660
    page.title = 'Calculadora Científica'
    page.window_always_on_top = True

    global resultados
    resultados = ft.Text(value='0', color=colors.WHITE, size=20)

    display = ft.Row(
        width=250,
        height=100,
        controls=[resultados],
        alignment='end'
    )

    botao = [ft.Container(
        content=ft.Text(value=botao['operador'], color=botao['font']),
        width=botao['largura'],
        height=botao['altura'],
        bgcolor=botao['fundo'],
        border_radius=10,
        border=borda,
        alignment=ft.alignment.center,
        on_click=select
    ) for botao in botoes]

    keybord = ft.Row(
        width=280,
        wrap=True,
        controls=botao,
        alignment='end'
    )

    page.add(display, keybord)


ft.app(target=pagina)
