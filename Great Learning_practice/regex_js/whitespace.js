/**
 * Write a JavaScript program to count number of words in string.

The script will be used to:

- Remove white-space from start and end position.
- Convert 2 or more spaces to 1.
- Exclude newline with a start spacing.
 */

let str = " The quick brown fox jumps over the lazy dog. ";
//remove whitespace from start & end 
const newstr = str.replace(/^\s|\s+$/,'');
//convert two or more spaces to 1
const newerStr = newstr.replace(/[\s]{2,}/gi,' ');
//exclude newline with start spacing
const final = newerStr.replace(/\n/,'\n');

console.log(newstr);
console.log(final.split(' '));
console.log(final.split(' ').length)
