// This is the reduce function
function thisIsReduce(array, combine, start) {
    let current = start;
    for (let element of array) {
      current = combine(current, element);
    }
    return current;
}
/*
The start value can be any data type. You could accumulate multiple arrays or objects together to result with a transformed object.
Or you could iterate through an array and accumalate a number or string.
*/

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
// console.log(getProductOfArray([2, 3, 4, 5]))


/*
Question 6: 
Write a function that takes an array of objects representing expenses, where
each object contains the expense amount and category. The function should calculate
the total expense amount for a specific category using the reduce() method and return the result.

Example Input:

const expenses = [
  { category: "Food", amount: 50 },
  { category: "Transportation", amount: 30 },
  { category: "Food", amount: 20 },
  { category: "Entertainment", amount: 40 },
  { category: "Food", amount: 10 },
];

Example Output:

const totalFoodExpense = calculateTotalExpense(expenses, "Food");
console.log(totalFoodExpense); // Output: 80

Approach:
O(n) time | O(1) space

Steps:
1. Iterate through array, start accumulator at 0
2. If input category exists in object, add amount to accumulator
3. return result
*/

function calculateTotalExpense(arr, specificCategory){
    return arr.reduce((totalAmount, expense) => (
        expense.category === specificCategory ? totalAmount + expense.amount : totalAmount
    ), 0)
}
const expenses = [
    { category: "Food", amount: 50 },
    { category: "Transportation", amount: 30 },
    { category: "Food", amount: 20 },
    { category: "Entertainment", amount: 40 },
    { category: "Food", amount: 10 },
  ];
// console.log(calculateTotalExpense(expenses, "Food")); // Output: 80

/*
Question 7:
Write a function that takes an array of book objects as input, where each
object represents a book and contains properties like title, author, and 
rating. The function should transform the input array into a new array of
book objects, where each object contains only the title and author properties
from the original book object.

Example Input:

const books = [
  { title: "The Great Gatsby", author: "F. Scott Fitzgerald", rating: 4.2 },
  { title: "To Kill a Mockingbird", author: "Harper Lee", rating: 4.5 },
  { title: "Pride and Prejudice", author: "Jane Austen", rating: 4.25 }
];

Example Output:

const simplifiedBooks = simplifyBookList(books);
console.log(simplifiedBooks);
// Output:
// [
//   { title: "The Great Gatsby", author: "F. Scott Fitzgerald" },
//   { title: "To Kill a Mockingbird", author: "Harper Lee" },
//   { title: "Pride and Prejudice", author: "Jane Austen" }
// ]


Apprach:
O(n) time | O(n) space

Steps:
1. Start accumulator as empty array
2. Iterate through input array, joining each element to the new array but only the title and author 
3. return result

*/

function simplifyBookList(arr){
    return arr.reduce((newList, book) => [...newList, {title: book.title, author:book.author}], [])
}
const books = [
    { title: "The Great Gatsby", author: "F. Scott Fitzgerald", rating: 4.2 },
    { title: "To Kill a Mockingbird", author: "Harper Lee", rating: 4.5 },
    { title: "Pride and Prejudice", author: "Jane Austen", rating: 4.25 }
];
// console.log(simplifyBookList(books))

/*
Question 8:
Write a function that takes an array of numbers as input and returns an object that contains
the count of each unique number in the array using the reduce() method. The unique numbers
should serve as keys in the object, and their counts should be the corresponding values.

Example Input: [1, 2, 3, 2, 1, 3, 4, 5, 4, 2]
Example Output: {1: 2, 2: 3, 3: 2, 4: 2, 5: 1}

Approach:
O(n) time | O(n) space

Steps:
1. Start accumulator from empty object
2. Iterate through input array, adding the count value to each unique number key
3. return the resulting object

*/

function countUniques(arr) {
    return arr.reduce((uniqueCount, number) => {
        uniqueCount[number] ? uniqueCount[number] += 1 : uniqueCount[number] = 1
        return uniqueCount
    }, {})
}
console.log(countUniques([1, 2, 3, 2, 1, 3, 4, 5, 4, 2]))


