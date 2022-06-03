var array = ["apple", "banana", "lemon", "mango"];

var result = array.reduce(
  (acc, v, i) => acc.concat(array.slice(i + 1).map((w) => v + " " + w)),
  []
);

console.log(result);
