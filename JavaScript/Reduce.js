/* 

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
    return arr.reduce((a, b) => a + b)
}
const numbers = [1, 2, 3, 4, 5];
console.log(sumArray(numbers))









// /* 
// Practice with recursive functions
// */

// // Write a function min that takes two arguments and returns their minimum.
// let smallestNumber = function min(num1, num2){
//     console.log("num1:", num1)
//     console.log("num2:", num2)
//    let minNum = Math.min(num1, num2)
//    console.log("Smallest num:", minNum)
//    return minNum;
// }

// console.log(smallestNumber(Math.floor(Math.random(0,1)*100), Math.floor(Math.random(0,1)*100)))
// console.log("")

// // We’ve seen that % (the remainder operator) can be used to test whether a 
// // number is even or odd by using % 2 to see whether it’s divisible by two. 
// // Here’s another way to define whether a positive whole number is even or odd:
// // 55
// // • Zero is even.
// // • One is odd.
// // • For any other number N, its evenness is the same as N - 2.
// // Define a recursive function isEven corresponding to this description. 
// // The function should accept a single parameter (a positive, whole number) and return a Boolean.
// // Test it on 50 and 75. See how it behaves on -1. Why? Can you think of a way to fix this?

// function isEven(num){
//     console.log(num)
//     if(num === 0){
//         return true
//     }
//     if(num === 1){
//         return false
//     }
//     num -= 2
//     isEven(num)
// }
// console.log("Test on 50:", isEven(50))
// console.log("Test on 75:", isEven(75))
