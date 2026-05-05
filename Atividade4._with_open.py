from dataclasses import dataclass
from os import system


def limpar_tela():
    system('cls')

@dataclass
class Funcionário:
    nome: str
    e_mail: str
    telefone: str

    def mostrar_dados(self):
        print('\nExibindo dados')
        print(f'Nome: {self.nome}')
        print(f'E-mail: {self.e_mail}')
        print(f'Telefone: {self.telefone}')

QUANTIDADE_FUNCIONARIOS = 2
lista_funcionario = []
print('Solicitando dados')
for i in range(QUANTIDADE_FUNCIONARIOS):
    novo_funcionario = Funcionário(
        nome=input('\nDigite seu nome: '),
        e_mail=input('Digite seu e-mail: '),
        telefone=input('Digite seu telefone: ')
)
    lista_funcionario.append(novo_funcionario)
    
limpar_tela()
print('\nExibindo dados')
for cliente in lista_funcionario:
    cliente.mostrar_dados()

with open('dados_funcionarios.txt', 'a', encoding='utf-8') as arquivo_funcionarios:
    for funcionarios in lista_funcionario:
        arquivo_funcionarios.write(f'{funcionarios.nome}, {funcionarios.e_mail}, {funcionarios.telefone}\n')
