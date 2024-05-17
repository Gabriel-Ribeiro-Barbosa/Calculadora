import flet as ft
from flet import border
from flet import colors
from decimal import Decimal
import math
#Definir botoes
botoes = [
    {'operador': 'tan','font':'#ffffff','fundo':'#575a5e','largura':60,'altura':50},
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

    {'operador': 'AC', 'font': '#000000', 'fundo': '#f9d12c','largura':131,'altura':50},
    {'operador': '%', 'font': '#000000', 'fundo': '#f9d12c','largura':60,'altura':50},
    {'operador': '/', 'font': '#000000', 'fundo': '#f9d12c','largura':60,'altura':50},

    {'operador': '7', 'font': '#f9d12c', 'fundo': '#000000','largura':60,'altura':50},
    {'operador': '8', 'font': '#f9d12c', 'fundo': '#000000','largura':60,'altura':50},
    {'operador': '9', 'font': '#f9d12c', 'fundo': '#000000','largura':60,'altura':50},

    {'operador': '*', 'font': '#000000', 'fundo': '#f9d12c', 'largura': 60, 'altura': 50},

    {'operador': '4', 'font': '#f9d12c', 'fundo': '#000000','largura':60,'altura':50},
    {'operador': '5', 'font': '#f9d12c', 'fundo': '#000000','largura':60,'altura':50},
    {'operador': '6', 'font': '#f9d12c', 'fundo': '#000000','largura':60,'altura':50},

    {'operador': '-', 'font': '#000000', 'fundo': '#f9d12c', 'largura': 60, 'altura': 50},

    {'operador': '1', 'font': '#f9d12c', 'fundo': '#000000','largura':60,'altura':50},
    {'operador': '2', 'font': '#f9d12c', 'fundo': '#000000','largura':60,'altura':50},
    {'operador': '3', 'font': '#f9d12c', 'fundo': '#000000','largura':60,'altura':50},

    {'operador': '+', 'font': '#000000', 'fundo': '#f9d12c', 'largura': 60, 'altura': 50},

    {'operador': '0', 'font': '#f9d12c', 'fundo': '#000000','largura':131,'altura':50},
    {'operador': '.', 'font': '#f9d12c', 'fundo': '#000000','largura':60,'altura':50},

    {'operador': '=', 'font': '#000000', 'fundo': '#f9d12c', 'largura': 60, 'altura': 50},
]


#Adicionar borda:
borda_superior = border.BorderSide(1, 'white')  # Borda superior branca de 1 pixel
borda_inferior = border.BorderSide(1, 'white')  # Borda inferior branca de 1 pixel
borda_lateral = border.BorderSide(1, 'white')   # Borda lateral branca de 1 pixel

# Instância para borda
borda = border.Border(top=borda_superior, bottom=borda_inferior, left=borda_lateral, right=borda_lateral)

lista_operadores = ['=','%','tan','sen','cos','sqrt','log','log10','e','pow','rad','pi','(',')']
def pagina(page: ft.Page): #Criar pagina
    page.bgcolor = colors.BLACK
    page.window_resizable = True#Permitir mobilidade
    page.window_width = 330  # Largura
    page.window_height = 660  # Altura
    page.title = 'Calculadora Científica'  # Título
    page.window_always_on_top = True  # Janela sempre visível

    resultados = ft.Text(value='0',color=colors.WHITE,size=20) #Definindo o resultado

    def avaliar_ex(expr):
        try:
            result = eval(expr, {"__builtins__": None},{ #__builtins é um dicionario interno que suporta funcoes e operacoes
                'tan': math.tan, #Tangente
                'sin': math.sin, #Seno
                'cos': math.cos, #Cosseno
                'sqrt': math.sqrt, #Raiz Quadrada
                'log': math.log, #Logaritimo
                'log10': math.log10, #Logaritimo de 10
                'pi': math.pi, #PI
                'e': math.e, #Constante e
                'pow': math.pow, #Potencia
                'rad': math.radians #Radianos
            })
            return result
        except:
            return 'Error'

    def calcular(ex):
        try:
            result = avaliar_ex(ex) #Chamando função de avaliar expressão
            if isinstance(result, float):
                digitos = min(abs(Decimal(result).as_tuple().exponent), 5)
                return format(result, f'.{digitos}f') # Formatar com 5 casas decimais
            return str(result) # Se o resultado não for um 'float', converte o resultado para string e retorna
        except:
            return 'Error'


    def select(event): #Função para clicar
        valor_atual = resultados.value if resultados.value not in ('0','Error') else '' #Verificar se o valor é 0
        value = event.control.content.value #Pegando o Valor
        #Verificando qual é o valor e suas propriedades após isso
        if value.isdigit() or value == '.':
            value = valor_atual + value
        elif value == 'AC':#Se for AC zera
            value = '0'
        elif value == '%':  # Se for porcentagem
            if '%' in valor_atual:  # Verificar se a porcentagem já foi aplicada
                return
            value = str(float(valor_atual) / 100)  # Converter para porcentagem
        elif value == '=':
            value = calcular(valor_atual) #Se for = significa que é para ativar os operadores
        else:
            value = valor_atual + value #Atualizando o valor

        resultados.value = value
        resultados.update() #Atualizar


    display = ft.Row( # Organizar uma linha
        width=250,
        height=100,
        controls=[resultados],
        alignment='end'
    )



    #Criando os botoes
    botao = [ft.Container(
        content=ft.Text(value=botao['operador'], color=botao['font']), #Referencia ao dicionario criado
        width= botao['largura'],
        height= botao['altura'],
        bgcolor=botao['fundo'],
        border_radius=10, #Aredondar
        border= borda,  # Borda
        alignment=ft.alignment.center, # Alinhar
        on_click=select  # Chamar função select
    )for botao in botoes]

    keybord = ft.Row(
        width=280,
        wrap=True,  # Quebrar linha
        controls=botao,
        alignment='end'
    )

    page.add(display,keybord)  # Adicionado o resultado

ft.app(target=pagina) #Executar