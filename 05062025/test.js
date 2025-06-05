var ime = 'Neko ime';
let dob = 26;
const PI = 3.14;

let broj = 42;
let tekst = 'Pozdrav!';
let istina = true;
let prazno = null;
let nepoznato;

let osoba = {ime:'Ive', dob: 24};

let brojevi = [1, 2, 3, 5];

let zbroj = 5 + 3;
let razlika = 5 - 3;

let i = true && false;
let ili = true || false;
let jednako = 5 == 5;
let identicno = 5 === 5;


if (dob > 18){
    console.log('Odrasla osoba!')
} else {
    console.log('Maloljetnik')
}

let boja = 'crvena';
switch (boja){
    case "crvena":
        console.log('CRVENA')
        break
    case "plava":
        console.log('PLAVA')
        break
    default:
        console.log('NEPOZNATO')
}

for (let i = 0; i < 5; i++){
    console.log(i)
}
console.log('*')
let j = 0;
while(j < 5){
    console.log(j);
    j++;
}
console.log('*')

let k = 0;
do{
    console.log(k);
    k++;
}while(k < 5)
console.log('*')


function pozdrav(ime){
    return 'Pozdrav, ' + ime; 
}

console.log(pozdrav('IVE!'))

let pozdrav2 = function(ime){
    return 'Pozdrav, ' + ime; 
}
console.log(pozdrav2('IVE!'))
