import os
from dataclasses import dataclass
os.system('cls')

@dataclass
class Empresa:
    nome: str
    cnpj: str
    telefone: str

    def mostrar_dados(self):
        print(f'Nome: {self.nome}')
        print(f'CNPJ: {self.cnpj}')
        print(f'Telefone: {self.telefone}\n')


QUANTIDADE_EMPRESAS = 1
lista_empresas = []

print('= Solicitando dados =')
for i in range(QUANTIDADE_EMPRESAS):
    nova_empresa = Empresa(
        nome=input('Digite seu nome: '),
        cnpj=input('Digite o CNPJ: '),
        telefone=input('Digite seu telefone: ')
    )
    print('')
    lista_empresas.append(nova_empresa)

print('= Salvando dados =')
with open('contato_empresas.csv', 'a', encoding='utf-8') as arquivo:
    for empresa in lista_empresas:
        arquivo.write(f'{empresa.nome}, {empresa.cnpj}, {empresa.telefone}\n')
    print('Salvo com sucesso!')

print('\n= Consultando arquivos =')
lista_contatos = []  # Limpar lista para recarregar do arquivo
with open('contato_empresas.csv', 'r') as arquivo2:
    for linha in arquivo2:
        nome, cnpj, telefone = linha.strip().split(', ')
        lista_contatos.append(Empresa(
            nome=nome,
            cnpj=cnpj,
            telefone=telefone
        ))
for contato in lista_contatos:
    contato.mostrar_dados()

print('= Fim do programa. =')