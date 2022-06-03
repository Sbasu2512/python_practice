//Write a JavaScript program to converts a specified number to an array of digits.

let num = 123;
const arr = [];
while(num > 0){
    digits = num%10;
    num = Math.floor(num/10);
    // console.log(num);
    arr.push(digits);
}

console.log(arr);