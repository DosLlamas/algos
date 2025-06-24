#include <iostream>
#include <vector>
#include <string>
using namespace std;

bool isPalindrome(string str){
    int l = 0;
    int r = str.length() - 1;
    while(l < r){
        if(str[l] != str[r]) return false;
        l++;
        r--;
    }
    return true;
}

// Function to check if a string is palindrome using recursion
bool isPalindromeRec(string str, int start, int end) {
    // Base case: if start index is greater than or equal to end, return true
    if (start >= end) 
        return true;

    // If characters at start and end are not the same, return false
    if (str[start] != str[end]) 
        return false;

    // Recursive call for the remaining substring
    return isPalindromeRec(str, start + 1, end - 1);
}


int main(){
    cout << boolalpha; // Print "true" or "false" instead of "1" or "0"
    cout << "Test 1 (Palindrome: 'racecar'): " << isPalindrome("racecar") << endl; // true
    cout << "Test 2 (Palindrome: 'tacocat'): " << isPalindrome("tacocat") << endl; // true
    cout << "Test 3 (Palindrome: 'a'): " << isPalindrome("a") << endl;             // true
    cout << "Test 4 (Palindrome: ''): " << isPalindrome("") << endl;               // true
    cout << "Test 5 (Non-Palindrome: 'hello'): " << isPalindrome("hello") << endl; // false
    cout << "Test 5 (Non-Palindrome: 'test'): " << isPalindrome("test") << endl; // false

    cout << boolalpha; // Print "true" or "false" instead of "1" or "0"
    cout << "Test 1 (Palindrome: 'racecar'): " << isPalindromeRec("racecar", 0, string("racecar").length() - 1) << endl; // true
    cout << "Test 2 (Palindrome: 'tacocat'): " << isPalindromeRec("tacocat", 0, string("tacocat").length() - 1) << endl; // true
    cout << "Test 3 (Palindrome: 'a'): " << isPalindromeRec("a", 0, string("a").length() - 1) << endl;             // true
    cout << "Test 4 (Palindrome: ''): " << isPalindromeRec("", 0, string("").length() - 1) << endl;               // true
    cout << "Test 5 (Non-Palindrome: 'hello'): " << isPalindromeRec("hello", 0, string("hello").length() - 1) << endl; // false
    cout << "Test 5 (Non-Palindrome: 'test'): " << isPalindromeRec("test", 0, string("test").length() - 1) << endl; // false
    return 0;
}
