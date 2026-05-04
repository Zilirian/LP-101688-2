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
        limpar_tela()
        print('\nExibindo dados')
        print(f'Nome: {self.nome}')
        print(f'E-mail: {self.e_mail}')
        print(f'Telefone: {self.telefone}')
       

lista_clientes = []
print('Solicitando dados')
for i in range(3):
    novo_cliente = Funcionário(
        nome=input('\nDigite seu nome: '),
        e_mail=input('Digite seu e-mail: '),
        telefone=input('Digite seu telefone: ')
)
    lista_clientes.append(novo_cliente)

print('\nExibindo dados')
for cliente in lista_clientes:
    cliente.mostrar_dados()
