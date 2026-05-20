
const vetorNum = [1, 2, 3, 4, 5];


function par_impar(a) {
    if (a % 2 !== 0) {
        return 'ímpar';
    } else {
        return 'par';
    }
}


vetorNum.forEach((num) => {
    console.log(`${par_impar(num)},`);
});