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

int main(){
    cout << boolalpha; // Print "true" or "false" instead of "1" or "0"
    cout << "Test 1 (Palindrome: 'racecar'): " << isPalindrome("racecar") << endl; // true
    cout << "Test 2 (Palindrome: 'tacocat'): " << isPalindrome("tacocat") << endl; // true
    cout << "Test 3 (Palindrome: 'a'): " << isPalindrome("a") << endl;             // true
    cout << "Test 4 (Palindrome: ''): " << isPalindrome("") << endl;               // true
    cout << "Test 5 (Non-Palindrome: 'hello'): " << isPalindrome("hello") << endl; // false
    cout << "Test 5 (Non-Palindrome: 'test'): " << isPalindrome("test") << endl; // false

    return 0;
}
