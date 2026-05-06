from dataclasses import dataclass

@dataclass
class Livro:
    nome:str
    autor: str
    categoria: str
    preco: float

    def mostrar_dados(self):
            print(f'Nome: {self.nome}')
            print(f'Autor: {self.autor}')
            print(f'Categoria: {self.categoria}')
            print(f'Preço: {self.preco}\n')