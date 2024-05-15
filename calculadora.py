import flet as ft
from flet import colors
from decimal import Decimal
#Criar um dicionario para facilitar a criação dos botões
botoes = [
    {'operador':'AC','font':'#ffffff','fundo':'#05c46b'},
    {'operador': '± ', 'font': '#ffffff', 'fundo': '#05c46b'},
    {'operador': '%', 'font': '#ffffff', 'fundo': '#05c46b'},
    {'operador': '/', 'font': '#ffffff', 'fundo': '#c40556'},
    {'operador': '7', 'font': '#000000', 'fundo': '#ffa500'},
    {'operador': '8', 'font': '#000000', 'fundo': '#ffa500'},
    {'operador': '9', 'font': '#000000', 'fundo': '#ffa500'},
    {'operador': '*', 'font': '#ffffff', 'fundo': '#c40556'},
    {'operador': '4', 'font': '#000000', 'fundo': '#ffa500'},
    {'operador': '5', 'font': '#000000', 'fundo': '#ffa500'},
    {'operador': '6', 'font': '#000000', 'fundo': '#ffa500'},
    {'operador': '-', 'font': '#ffffff', 'fundo': '#c40556'},
    {'operador': '1', 'font': '#000000', 'fundo': '#ffa500'},
    {'operador': '2', 'font': '#000000', 'fundo': '#ffa500'},
    {'operador': '3', 'font': '#000000', 'fundo': '#ffa500'},
    {'operador': '+', 'font': '#ffffff', 'fundo': '#c40556'},
    {'operador': '0', 'font': '#000000', 'fundo': '#ffa500'},
    {'operador': '.', 'font': '#000000', 'fundo': '#ffa500'},
    {'operador': '=', 'font': '#ffffff', 'fundo': '#05c48c'},
]

def pagina(page: ft.Page): #Configuração da página
    page.bgcolor = '#f0f0f0' #Cor de fundo
    page.window_resizable = False #Não permitir que o usuario redimencione a tela
    page.window_width = 280 #Largura
    page.window_height = 380 #Altura
    page.title = 'Calculadora' #Título
    page.window_always_on_top = True #Janela sempre visível

    resultados = ft.Text(value='0',color='#000000',size=20) #Definindo o resultado

    #Criando uma função para calculuar os resuldaos

    def calculator(operador,valor_atual):
        try:
            value = eval(valor_atual) #Eval faz contas aritmeticas

            if operador == '%': #Calular porcentagem
                value /= 100
            elif operador == '±':
                value = -value #Inverter o sinal
        except:
            return 'Error' #Erro ao dividir por 0

        digitos = min(abs(Decimal(value).as_tuple().exponent),5) #Limitar digitos
        return format(value,f'.{digitos}f') #Formatando com a variavel digitos
    def select(event): #Função para clicar
        valor_atual = resultados.value if resultados.value not in ('0','Error') else '' #Verificar se o valor é 0
        value = event.control.content.value #Pegando o Valor
        #Verificando qual é o valor e suas propriedades após isso
        if value.isdigit():
            value = valor_atual + value
        elif value == 'AC':#SE for AC zera
            value = '0'
        else: #Verificar se é um operador
            if valor_atual and valor_atual[-1] in ('/','*','-','+','.'): #Valor_atual[-1] -> ultimo valor digitado
                valor_atual = valor_atual[:-1] #Valor_atual[:-1] -> substitui pelo ultimo elemento digitado

            value = valor_atual + value #Atualizando o valor

            if value[-1] in ('=','%','±'): #Verificando se vai aver calcululo
                value = calculator(operador=value[-1],valor_atual=valor_atual)

        resultados.value = value
        resultados.update() #Atualizar

    display = ft.Row( #Organizar uma linha
        width=250,
        controls=[resultados],
        alignment='end'
    )

    #Criando um botão

    b = [ft.Container(
        content=ft.Text(value= b['operador'],color=b['font']),
        width=50,
        height=50,
        bgcolor=b['fundo'],
        border_radius = 100, #Borda
        alignment= ft.alignment.center,
        on_click = select  #Chamar função select
    )for b in botoes]

    keybord = ft.Row(
        width=250,
        wrap= True,#Quebrar linha
        controls =b,
        alignment='end'
    )
    page.add(display,keybord) #Adicionado o resultado


ft.app(target=pagina) #Executar