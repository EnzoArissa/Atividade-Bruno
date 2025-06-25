def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Divisão por zero não é permitida."

def potencia(base, expoente):
    return base ** expoente

def raiz_quadrada(numero):
    if numero >= 0:
        return numero ** 0.5
    else:
        return "Número negativo não possui raiz real."

def media(*numeros):
    return sum(numeros) / len(numeros)

def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)

def area_retangulo(base, altura):
    return base * altura

def area_triangulo(base, altura):
    return 0.5 * base * altura

def hipotenusa(cateto_a, cateto_b):
    return (cateto_a ** 2 + cateto_b ** 2) ** 0.5

def area_quadrado(lado):
    return lado ** 2

def volume_cubo(aresta):
    return aresta ** 3

def juros_simples(capital, taxa, tempo):
    juros = capital * taxa * tempo
    montante = capital + juros
    return juros, montante

def juros_compostos(capital, taxa, tempo):
    montante = capital * (1 + taxa) ** tempo
    juros = montante - capital
    return juros, montante

def inverter_string(texto):
    return texto[::-1]

def maiusculas_minusculas(texto):
    return texto.upper(), texto.lower()

def substituir_substring(texto, antigo, novo):
    return texto.replace(antigo, novo)

def remover_espacos(texto):
    return texto.strip()

def contar_ocorrencias(texto, substring):
    return texto.count(substring)

def capitalizar_palavras(texto):
    return texto.title()

def centralizar_texto(texto, largura_total):
    return texto.center(largura_total)

def adicionar_zeros(numero, largura_total):
    return f"{numero:0>{largura_total}}"

def dividir_texto(texto, delimitador):
    return texto.split(delimitador)

def juntar_texto(lista_strings, separador):
    return separador.join(lista_strings)

def cor_texto(texto, cor):
    cores = {
        'vermelho': '\033[91m',
        'verde': '\033[92m',
        'amarelo': '\033[93m',
        'azul': '\033[94m',
        'roxo': '\033[95m',
        'azul claro': '\033[96m',
        'reset': '\033[0m'
    }
    return cores.get(cor, '') + texto + cores['reset']

def desenhar_gato():
    gato = r"""
 /\_/\  
( o.o ) 
 > ^ <
"""
    return gato

def desenhar_cachorro():
    cachorro = r"""
   / \__
  (    @\____
  /         O
 /   (_____/
/_____/   U
"""
    return cachorro

def desenhar_peixe():
    peixe = r"""
><(((º>
"""
    return peixe

def desenhar_tartaruga():
    tartaruga = r"""
  ___
 /0  \
 \___/
"""
    return tartaruga

def desenhar_leao():
    leao = r"""
   \    ____
    \  /    \
      | ^  ^ |
      |      |
       \____/
"""
    return leao

def desenhar_cavalo():
    cavalo = r"""
      ,/'  | 
     ( =   | 
      / |  |
      | ^  |
     /  -  \ 
    /  -  \ \
   ( ~    ) )
    \    / /
     |  | | 
    / ^  | \
   /_/ |_/  
"""
    return cavalo

def emoji_sorrindo():
    return "😊"

def emoji_triste():
    return "😢"

def emoji_coracao():
    return "❤️"

def emoji_palmas():
    return "👏"

def emoji_pizza():
    return "🍕"

def emoji_riso():
    return "😄"

def emoji_chorando_de_ri():
    return "😂"

def emoji_surpreso():
    return "😮"

def emoji_piscadela():
    return "😉"

def emoji_amor():
    return "🥰"