let reg = /sayantan/ ; //pattern to look for
// reg = /sayantan/g ; //g flag means global
// reg = /sayantan/i  //i flag denotes case sensitivity
// reg = /sayantan/gi ; //we can put two flags like so
const string = "Hello my name is sayantan and with SayaNtan" ; //String we are looking pattern in.

//1. exec() --> will give us an array of matches
let result = reg.exec(string);
// console.log(result);
reg.exec(string);
result = reg.exec(string);
// console.log(result);

//2. test() --> will give boolean for a match 
result = reg.test(string);
// console.log(result)

//3. match() --> will return an array of result or null
result = string.match(reg);
// console.log(result);

//4. search() --> will return index of first match or -1
result = string.search(reg);
// console.log(result);

//5. replace() --> will replace the word, it takes two params, search param, replace param; all matches
result = string.replace(reg, "Sayan");
console.log(result);

