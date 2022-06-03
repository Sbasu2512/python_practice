let str = "4458695403293";  //13 digits
// str = "sayanbasu098@yahoo.co.in";
// regex = /^(?:4[0-9]){12}$/ ;
// regex = /^[0-9]{15}$/
str  = "19-20.2500"
//email problem
// regex = /^([a-zA-Z])([a-zA-z0-9]+)([._-]?)([a-zA-Z0-9]+)([@])([a-zA-Z]+)([.])([a-zA-z]+)([.])?([a-zA-z]+)?$/
//credit card problem - following does not work
// regex= /^((4[0-9]{12}([0-9]{3})|(5[1-5][0-9]{14})|(6011[0-9]{12})|(5[0-9]{14})|3[068][0-9]{11}|(2131[0-9]{11})|1800[0-9]{11}|(35[0-9]{14}))$/
//visa card
/**
 It should be 13 or 16 digits long, new cards have 16 digits and old cards have 13 digits.
It should be starts with 4.
If the cards have 13 digits the next twelve digits should be any number between 0-9.
If the cards have 16 digits the next fifteen digits should be any number between 0-9.
It should not contains any alphabets and special characters.
 */
regex = /^4[0-9]{12}([0-9]{3})?$/
//date-string checker
regex = /^(([0-9]{2}([0-9]{2})?)[./-]?[0-9]{2}[./-]?[0-9]{2,4})$/
//remove whitespace
// regex = /^\s|\s+$/

console.log(regex.test(str));

console.log(regex.exec(str));
//trim function using regex
// console.log(str.replace(/^\s+|\s+$/,''))
