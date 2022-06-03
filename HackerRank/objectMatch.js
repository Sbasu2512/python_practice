function isObjEqual(obj1, obj2){
    //check if the length of keys are equal or not
    obj1keys = Object.keys(obj1); 
    obj2keys = Object.keys(obj2);

    obj1keys.length !== obj2keys.length ? false : true
    // loop over any one of the obj keys to match the values
    for(let objkey of obj1keys){
        if(obj1[objkey] === obj2[objkey]){
            return true
        } else {
            return false
        }
    }
}

const obj1 = {
    'a':1,
    'b':2
}

const obj2 = {
    'a' : 1,
    'b' : 2
}

isObjEqual(obj1, obj2);