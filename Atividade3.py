from dataclasses import dataclass
from os import system

def limpar_tela():
    system('cls')

@dataclass
class Pet:
    nome: str
    idade: int
    raca: str

    def mostrar_dados(self):
        print('\nExibindo dados')
        print(f'Nome: {self.nome}')
        print(f'Idade: {self.idade}')
        print(f'Raça: {self.raca}')
       
lista_pets = []

def mostrar_dados_pets():
    print('\nExibindo dados')
    for pet in lista_pets:
        pet.mostrar_dados( )

def main():
    while True:
        limpar_tela()
        print('Você deseja adicionar um novo Pet? (s/n)')
        resposta = input().lower()
        if resposta == 's':
            novo_pet = Pet(
                nome=input('\nDigite o nome do pet: '),
                idade=int(input('Digite a idade do pet: ')),
                raca=input('Digite a raça do pet: ')
            )

            lista_pets.append(novo_pet)
        elif resposta == 'n':
            break
        else:
            print('Resposta inválida. Por favor, digite "s" para sim ou "n" para não.')
    
    mostrar_dados_pets()
    with open('dados_pets.txt', 'a') as arquivo_pets:
        for pets in lista_pets:
            arquivo_pets.write(f'{pets.nome}, {pets.idade}, {pets.raca}\n')

if __name__ == "__main__":
    main()