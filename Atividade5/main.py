from os import system
from Models import Empresa
from time import sleep

def limpar_tela():
    system('cls')

lista_empresas = []
while True:
    limpar_tela()
    print('Você deseja adicionar uma empresa? (s/n)')
    escolha = input()
    if escolha.lower() == "s":
        nova_empresa = Empresa(
            nome=input('Digite o nome da empresa: '),
            cnpj=int(input('Digite o cnpj da empresa: ')),
            telefone=input('Digite o telefone da empresa: ')
            )
        print('Empresa adicionada com sucesso!')
        sleep(3)
        lista_empresas.append(nova_empresa)
    elif escolha.lower() == 'n':
        break
    else:
        continue

with open('contato_empresas.csv', 'a', encoding='utf-8') as contato_empresas:
    for empresas in lista_empresas:
        contato_empresas.write(f'{empresas.nome}, {empresas.cnpj}, {empresas.telefone}')