
const numero = 5


function par_impar(a) {
    if (a % 2 !== 0) {
        return 'ímpar'
    } else {
        return 'par'
    }
}

let c = par_impar(numero)
console.log(`O número é ${c}`)