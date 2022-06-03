//find max num from a list of an array

const list = [10, 9, 6, 98, 4, 3, 2];
max_num = 0;
for(i=0; i<list.length; i++){
    if(list[i] > max_num){
        max_num = list[i];
    }
}
console.log(max_num);