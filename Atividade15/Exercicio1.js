
const a = 5
const b = 5

function soma (a, b) {
	return a + b
}
function multiplicacao (a, b) {
	return a * b
}



if (a === b) {
	c = soma(a, b)
	console.log(`O valor de C é: ${c}`)
} else {
	c = multiplicacao(a, b)
	console.log(`O valor de C é: ${c}`)
}