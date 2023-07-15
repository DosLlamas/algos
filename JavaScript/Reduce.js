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
Question 3:
Write a JavaScript function called flattenArray that takes an array 
of arrays and returns a single flattened array that contains all
the elements from the nested arrays. The order of elements should be preserved.

Example usage:

const nestedArray = [[1, 2], [3, 4], [5, 6]];
console.log(flattenArray(nestedArray)); // Output: [1, 2, 3, 4, 5, 6]

Apprach:
O(n) time
O(m) space where m is the total length of elements from each nested array

Steps:
1. define empty result array in reduce argument
2. iterate and push each element in each array to the result array
3. return result

*/

function flattenArray(arr){
    // Both of these soltions work
    // return arr.reduce((result, currentArray) => [result.concat(currentArray)], [])
    return arr.reduce((result, currentArray) => [...result, ...currentArray], [])
}
const nestedArray = [[1, 2], [3, 4], [5, 6]];
// console.log(flattenArray(nestedArray)); // Output: [1, 2, 3, 4, 5, 6]



/*
Question 4: 
Write a function that takes an array of objects representing students, 
where each object contains the student's name and their score. The function 
should calculate the average score of all the students using the reduce() 
method and return the result.

Example Input:

var students = [
  { name: "Alice", score: 85 },
  { name: "Bob", score: 90 },
  { name: "Charlie", score: 75 },
  { name: "David", score: 92 },
];

Example Output:
var averageScore = calculateAverageScore(students);
console.log(averageScore); // Output: 85.5

Approach:
O(n) time
O(1) space

Steps:
1. Iterate over array, adding up sum of each score
2. Divide by the array length at the end and return result

*/

function getAverageStudentScore(arr){
    return arr.reduce((sum, student) => sum + student.score, 0) / arr.length
}
const students = [
    { name: "Alice", score: 85 },
    { name: "Bob", score: 90 },
    { name: "Charlie", score: 75 },
    { name: "David", score: 92 },
  ];
// console.log(getAverageStudentScore(students))


/*
Question 5: 
Write a function that takes an array of numbers as input and returns
the product of all the numbers using the reduce() method.

Example Input: [2, 3, 4, 5]
Example Output: 120

Approach:
O(n) time
O(1) space

Steps:
1. if array length is 0, return 0
2. start an accumlator at 1
3. Iteratate through array, multiplying each element against the accumulator 
4. return result

*/

function getProductOfArray(arr){
    if(arr.length === 0) return 0
    return arr.reduce((totalProduct, element) => totalProduct * element, 1)
}
console.log(getProductOfArray([2, 3, 4, 5]))