const vetor_notas = [10, 10, 10];

const tamanho = vetor_notas.length;

const total = vetor_notas.reduce((soma, atual) => soma + atual, 0);
console.log(total);

const media = total / tamanho;

console.log(media);