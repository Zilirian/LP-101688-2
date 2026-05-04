from dataclasses import dataclass
from os import system 

def limpar_tela():
    system('cls')

@dataclass
class Cliente:
    nome: str
    idade: int
    peso: float
    altura: float

    def mostrar_dados(self):
        print('\nExibindo dados')
        print(f'Nome: {self.nome}')
        print(f'Idade: {self.idade}')
        print(f'Peso: {self.peso}')
        print(f'Altura: {self.altura}')

lista_clientes = []
print('Solicitando dados')
for i in range(2):
    novo_cliente = Cliente(
        nome=input('\nDigite seu nome: '),
        idade=int(input('Digite sua idade: ')),
        peso=float(input('Digite seu peso: ')),
        altura=float(input('Digite sua altura: '))
)
    lista_clientes.append(novo_cliente)

print('\nExibindo dados')
for cliente in lista_clientes:
    cliente.mostrar_dados()


