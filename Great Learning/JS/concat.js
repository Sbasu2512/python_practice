function stringConcat(arr) {
    // your code here 
   return arr.reduce((acc, item)=>{
       
        // console.log(acc + String(item))
        acc = acc + String(item);
        return acc
   }, ' ')
 }
 
 console.log(stringConcat([1,2,3,4])); 