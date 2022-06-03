var array = ["apple", "banana", "lemon", "mango"];

var result = array.reduce(
  (acc, v, i) => acc.concat(array.slice(i + 1).map((w) => console.log(w))),
  []
);

// const result = array.reduce((acc,item,index) => {
//     console.log(acc.concat(array.slice(index+1).map(w => item + " " + w )))
//     // return acc.concat(array.slice(index+1))
// },[])


// console.log(result);
