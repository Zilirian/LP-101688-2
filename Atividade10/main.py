from dataclasses import dataclass
from os import system

CSV_FILE = 'pedidos.csv'

@dataclass
class Pedido:
    numero: int
    cliente: str
    item: str
    quantidade: int

    def gravar(self):
        with open(CSV_FILE, 'a', newline='', encoding='utf-8') as arquivo:
            novo_pedido = Pedido(numero=input('\nDigite o nome do pedido: '),
                            cliente=input('Digite o nome do cliente: '),
                            item=input('Digite o  nome do item: '),
                            quantidade=int(input('Digite a quantidade: ')))
            arquivo.write(f'{novo_pedido.nome}, {novo_pedido.autor}, {novo_pedido.categoria}, {novo_pedido.preco}\n')
            print('\nSalvo com sucesso!')


def limpar_tela():
    system('cls')


def ler_numero_inteiro(pergunta):
    while True:
        valor = input(pergunta).strip()
        if valor.isdigit():
            return int(valor)
        print('Digite um número inteiro válido.')


def menu():
    print('''
--- MENU ---
1. Adicionar Pedidos
2. Listar Pedidos
3. Sair

''')
    return input('Escolha uma opção: ').strip()


def adicionar_pedido():
    limpar_tela()
    print('--- Adicionar Pedido ---')
    numero = ler_numero_inteiro('Digite o número do pedido: ')
    cliente = input('Nome do cliente: ').strip()
    item = input('Item solicitado: ').strip()
    quantidade = ler_numero_inteiro('Quantidade: ')

    pedido = Pedido(numero, cliente, item, quantidade)
    pedido.gravar()
    print('\nPedido gravado com sucesso!')
    input('Pressione Enter para voltar ao menu...')

lista_pedidos = []
def ler_pedidos():
    limpar_tela()
    print('--- Pedidos Gravados ---')
    try:
        with open(CSV_FILE, 'r', newline='', encoding='utf-8') as arquivo2:
            for linha in arquivo2:
                nome, autor, categoria, preco = linha.strip().split(', ')
                lista_pedidos.append(Pedido(
                    nome=nome,
                    autor=autor,
                    categoria=categoria,
                    preco=preco
                ))
        for pedido in lista_pedidos:
            pedido.mostrar_dados()
    except FileNotFoundError:
        pedidos = []

    if not pedidos:
        print('Nenhum pedido encontrado.')
    else:
        for linha in pedidos:
            if len(linha) >= 4:
                numero, cliente, item, quantidade = linha
                print(f'Pedido {numero} - Cliente: {cliente} - Item: {item} - Qtde: {quantidade}')
            else:
                print('Linha inválida no arquivo:', linha)

    input('\nPressione Enter para voltar ao menu...')


def main():
    while True:
        limpar_tela()
        opcao = menu()

        if opcao == '1':
            adicionar_pedido()
        elif opcao == '2':
            ler_pedidos()
        elif opcao == '3':
            print('Encerrando o sistema...')
            break
        else:
            print('Opção inválida. Digite 1, 2 ou 3.')
            input('Pressione Enter para continuar...')


if __name__ == '__main__':
    main()