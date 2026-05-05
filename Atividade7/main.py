import os
from dataclasses import dataclass
os.system('cls')

@dataclass
class Funcionario:
    nome: str
    e_mail: str
    telefone: str

    def mostrar_dados(self):
        print('\nExibindo dados')
        print(f'Nome: {self.nome}')
        print(f'E-mail: {self.e_mail}')
        print(f'Telefone: {self.telefone}')

lista_funcionarios = []
with open('dados_funcionarios.csv', 'r') as arquivo:
    for linha in arquivo:
        nome, e_mail, telefone = linha.strip().split(', ')
        lista_funcionarios.append(Funcionario(
            nome=nome,
            e_mail=e_mail,
            telefone=telefone
        ))

for linha in lista_funcionarios:
    linha.mostrar_dados()