function sinais(numero) {
    if (numero < 0) {
        return 'negativo'
    } if (numero > 0) {
        return 'positivo'
    } else {
        return 'neutro'
    }
}

sinal = sinais(0)
console.log(`O número é ${sinal} `)

