from Uteis import *

lista_livros = []
lista_emprestimo = []

def cadastrar_livro():
    try:
        qt_livros_rgt = int(input('Digite quantos livros deseja registrar: '))
    except ValueError:
        print('Valor invalido, digite um número.')
        return
    for v in range(qt_livros_rgt):
        titulo = str(input('Informe o título do livro: '))

        try:
            estoque = int(input('Informe a quantidade de livros disponivel no estoque: '))
            while estoque <= 0:
                print('Valor inválido.')
                estoque = int(input('Informe a quantidade de livros: '))
        except ValueError:
            print('Entrada inválida, digite um número')
            return

        autor = str(input('Digite qual o autor do livro: '))
        genero = str(input('Digite o gênero do livro: '))

        alternativa_genero = str(input('Deseja colocar um subgênero1? [S/N]: '))
        genero2 = 'não possui'
        if alternativa_genero.lower() == 's':
            genero2 = str(input('Digite o subgênero: '))
        global livro
        livro = {
            'titulo': titulo,
            'autor': autor,
            'genero': genero,
            'estoque': estoque,
            'segundo_genero': genero2,
        }
        lista_livros.append(livro)
        print('Livro cadastrado com sucesso.\n')

def registrar_emprestimo():
    for livro in lista_livros:
        print(f"Titulo:{livro['titulo']} | Gênero :{livro['genero']} | "
              f"Segundo genero : {livro['segundo_genero']} | Numero de Livros Disponiveis :{livro['estoque']}")
    titulo_livro = str(input('Digite o titulo do livro: ')).lower()
    for livro in lista_livros:
     if livro["estoque"]==0:
        print('fora de estoque')
        return
     if titulo_livro.lower() in livro["titulo"].lower():
      data = str(input('Digite a data de devolução do livro: '))
      nome_aluno = str(input('Digite o nome do aluno que fez o emprstimo: '))
      livro["estoque"] -= 1

def buscar_livros():
    termo_busca = str(input('Buscar por Titulo do livro ou Gênero:')).lower()
    encontrado = []
    for livro in lista_livros:
        if (termo_busca in livro["titulo"].lower()) or (termo_busca in livro['genero'].lower()) or (termo_busca in livro['segundo_genero'].lower()):
            encontrado.append(livro)
    if len(encontrado) == 0:
        print('Nenhum livro encontrado.')
        return
    numero = 1
    for livro in encontrado:
        print(f"[{numero}]Titulo:{livro['titulo']} | Gênero :{livro['genero']} | "
              f"Segundo genero : {livro['segundo_genero']} | Numero de Livros Disponiveis :{livro['estoque']}")
        numero += 1
    print()

def devolutiva_livros():
    retorno_livro = []
    if len(lista_livros) == 0:
        print('Nenhum livro cadastrado. \n')
        return
    numero = 1
    for livro in lista_livros:
     try:
        retorno_livro.append(livro)
        print(f"[{numero}] Titulo:{livro['titulo']} | Gênero :{livro['genero']} | "
              f"Segundo genero : {livro['segundo_genero']} | Numero de Livros Disponiveis :{livro['estoque']}")
        numero += 1
        indice = numero - 1
        escolha_sim = str(input('Esse livro já foi devolvido? [S/N]:'))
        if escolha_sim== 's' or escolha_sim== 'S':
         livro["estoque"] += 1
     except ValueError:
        print('Valor invalido, coloque outo numero')
    if numero <= len(lista_livros):
     print('Devolutiva marcada como realizada')

def menu_biblioteca():
    while True:
        print(f'    {cor_texto('   |----------------------|\n'
                                '      | 🧮Biblioteca_Digital🧮 |\n'      
                                '       |----------------------| ', 'azul')}')

        escolha_funcao = str(input(
                                   f'\n'
                                   f'{cor_texto("[1]", "amarelo")} Cadastrar livro\n'
                                   f'{cor_texto("[2]", "amarelo")} Registrar emprestimo\n'
                                   f'{cor_texto("[3]", "amarelo")} Buscar livros\n'
                                   f'{cor_texto("[4]", "amarelo")} Devolutiva livros\n'
                                   f'{cor_texto("[5]", "amarelo")} Sair\n'
                                   f'Escolha qual das funções você quer utilizar: '))
        if escolha_funcao == '1':
            cadastrar_livro()
        elif escolha_funcao == '2':
            registrar_emprestimo()
        elif escolha_funcao == '3':
            buscar_livros()
        elif escolha_funcao == '4':
            devolutiva_livros()
        elif escolha_funcao == '5':
            print('Saindo do sistema, bye bye Bruon')
            break
        else:
            print('Opção invalida, digite uma das opções apresentadas.')

menu_biblioteca()