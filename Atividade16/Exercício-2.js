// CRIANDO UM VETOR
const vetor_numeros = [10, 20, 30, 40, 50]

console.log('Listando todos os elementos do vetor')
console.log(vetor_numeros)

console.log('\nMultiplicando cada elementos do vetor por 2:')
const dobrados = vetor_numeros.map(n => n * 2)
console.log(dobrados)
console.log(vetor_numeros)

console.log('\n Filtrando elementos ímpares')
vetor_numeros.push(1)
vetor_numeros.push(3)
const impares = vetor_numeros.filter(n => n % 2 == 1)
console.log(impares)

console.log('\n Filtrando elementos negativos')
vetor_numeros.push(-5)
vetor_numeros.push(-15)
const negativos = vetor_numeros.filter(n => n < 0)
console.log(negativos)

console.log('\n Somando todos os elementos do vetor: ')
const total = vetor_numeros.reduce((soma, atual) => soma + atual, 0)
console.log(total)