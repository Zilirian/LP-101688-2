from os import system
from models import Livro
import time

def limpar_tela():
    system('cls')

def menu():
    print('''
          -----------------------MENU-----------------------
          Adicionar livro                         - Digite 1
          Listar livros                           - Digite 2
          Sair                                    - Digite 3
          ''')
    while True:
        try:
            opcao = int(input('\nDigite a opção desejada: '))
            break
        except ValueError:
            print('Deve ser um número')
            time.sleep(3)
            limpar_tela()
    return opcao

def adicionar_livro():
    
    with open('catalogo_livros.csv', 'a', encoding='utf-8') as arquivo:
        novo_livro = Livro(nome=input('\nDigite o nome do livro: '),
                            autor=input('Digite o nome do autor: '),
                            categoria=input('Digite a categoria do livro: '),
                            preco=float(input('Digite o preço do livro: ')))
        arquivo.write(f'{novo_livro.nome}, {novo_livro.autor}, {novo_livro.categoria}, {novo_livro.preco}\n')
        print('\nSalvo com sucesso!')

def listar_livros():
        lista_contatos = []
        with open('catalogo_livros.csv', 'r', encoding='utf-8') as arquivo2:
            for linha in arquivo2:
                nome, autor, categoria, preco = linha.strip().split(', ')
                lista_contatos.append(Livro(
                    nome=nome,
                    autor=autor,
                    categoria=categoria,
                    preco=preco
                ))
        for contato in lista_contatos:
            contato.mostrar_dados()

def filtro_opcoes(opcao):
    match opcao:
        case 1:
            limpar_tela
            adicionar_livro()
        case 2:
            limpar_tela()
            listar_livros()
        case 3:
            limpar_tela()
            exit()

def main():
    limpar_tela()
    while True:
        opcao = menu()
        filtro_opcoes(opcao)

if __name__ == "__main__":
    main()