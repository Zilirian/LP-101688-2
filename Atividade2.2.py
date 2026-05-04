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
       
lista_funcionarios = []

def mostrar_dados_clientes():
    print('\nExibindo dados')
    for cliente in lista_funcionarios:
        cliente.mostrar_dados( )

def main():
    while True:
        limpar_tela()
        print('Você deseja adicionar um novo funcionário? (s/n)')
        resposta = input().lower()
        if resposta == 's':
            novo_funcionario = Funcionário(
                nome=input('\nDigite seu nome: '),
                e_mail=input('Digite seu e-mail: '),
                telefone=input('Digite seu telefone: ')
            )

            lista_funcionarios.append(novo_funcionario)
        elif resposta == 'n':
            break
        else:
            print('Resposta inválida. Por favor, digite "s" para sim ou "n" para não.')
    
    for funcionario in lista_funcionarios:
        funcionario.mostrar_dados()
if __name__ == "__main__":
    main()