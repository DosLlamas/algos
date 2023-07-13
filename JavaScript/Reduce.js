/* 
Question 1:

Practice with built-in reduce() method

Write a JavaScript function called sumArray that takes an 
array of numbers as input and returns the sum of all the numbers 
in the array using the reduce() method.

Example usage:

javascript
const numbers = [1, 2, 3, 4, 5];

console.log(sumArray(numbers)); // Output: 15

*/

function sumArray(arr){
    return arr.reduce((a, b) => a + b) // reduce(array, any function, start value) takes 3 parameters but you can leave the start value blank if your array has at least one element
}
const numbers = [1, 2, 3, 4, 5];
// console.log(sumArray(numbers))

/*
Question 2:

Write a JavaScript function called getAverageAge that takes an array
of objects representing people and returns the average age of all 
the people. Each object in the array has a name property and an age property.

Example usage:

const people = [
  { name: "John", age: 25 },
  { name: "Jane", age: 30 },
  { name: "Mark", age: 20 },
  { name: "Emily", age: 35 },
];

console.log(getAverageAge(people)); // Output: 27.5

Approach:
O(n) time
O(1) space

Steps:
1. Iterate over array, and sum up all of the ages
2. Divide by the array.length
*/

// This is the reduce function
// function reduce(array, combine, start) {
//     let current = start;
//     for (let element of array) {
//       current = combine(current, element);
//     }
//     return current;
// }
function getAverageAge(arr){
    return arr.reduce((sum, person) => sum + person.age, 0) / arr.length
}

const people = [
    { name: "John", age: 25 },
    { name: "Jane", age: 30 },
    { name: "Mark", age: 20 },
    { name: "Emily", age: 35 },
]
// console.log(getAverageAge(people)); // Output: 27.5

/*
Question:
Write a JavaScript function called flattenArray that takes an array 
of arrays and returns a single flattened array that contains all
the elements from the nested arrays. The order of elements should be preserved.

Example usage:

const nestedArray = [[1, 2], [3, 4], [5, 6]];
console.log(flattenArray(nestedArray)); // Output: [1, 2, 3, 4, 5, 6]

Apprach:
O() time
O() space

Steps:
1. 

*/



