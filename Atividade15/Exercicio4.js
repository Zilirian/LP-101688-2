const vetorNomes = ['Marta', 'Jóse', 'Mario']

console.log('Exibindo todos os elementos')
console.log(vetorNomes)

console.log('\nAdicionando um elemento')
vetorNomes.push('Mariana')
console.log(vetorNomes)

// pop = remove o último da lista, shift = remove o primeiro da lista, unshift = adiciona no inicio da lista, push = adiciona ao final da lista 

// forEach = laco de repticao

vetorNomes.forEach((nome, index) => {
    console.log(`${index}: ${nome}`);
});
