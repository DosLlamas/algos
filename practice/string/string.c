#include <stdio.h>
#include <stdlib.h>
#include <string.h>  // Include the string functions

// Prototype functions
void readingInput();
void firstWay();
void secondWay();
void thirdWay();
void commonMethods();

int main(){
    // firstWay();
    // secondWay();
    // thirdWay();
    commonMethods();
    // readingInput();
    return 0;
}
void readingInput(){
    // Read input, limiting to 99 characters (+1 for null terminator)
    char test[100];
    printf("Enter a string:\n");
    scanf("%s", test);  
    printf("You entered: %s\n", test);
}
void firstWay(){
    // You can declare and assign at the beginning like this:
    char* str0 = "This is string 1";
    // If you don't want to assign in the beginning, always initialize pointers to NULL:
    char* str1 = NULL; 
    // Then you can reassign later:
    str1 = "This is string 1";
    str1 = "This is a new string";
    // You cannot change each index individually:
    // str1[0] = 't';
    // You cannot use strcpy(variable, newString):
    // strcpy(str1, "This is string 1");
    printf("str1: %s\n", str1);
}
void secondWay(){
    // You can declare and assign: 
    char str2[] = "This is string 2";
    // You cannot reassign: str2 = "This is a new string";
    // But you can change each index individually, or you could use a loop:
    str2[0] = 't';
    // You should not access the last element, the null terminator('\0'), nor go out of bounds or risk errors:
    // str2[17] = 'o'; // Do not change the null terminator, '\0'
    // str2[234] // Do not go out of bounds.
    printf("str2: %s\n", str2);
    // Here is another way to declare and assign:
    char str3[] = {'H', 'i', '\0'};
    // You can change the index here as well:
    str3[0] = 'h';
    printf("str3: %s\n", str3);
    // If you don't want to assign at the beginning:
    char str4[10];
    // Then change each indices later, but don't forget the null terminator nor go out of bounds or risk errors:
    str4[0] = 'H';
    str4[1] = 'i';
    str4[2] = '\0';
    // You can also use strcpy(variable, newString) to reassign: 
    // But make sure your new string is within bounds of size, including the null terminator
    strcpy(str4, "hi");
    printf("str4: %s\n", str4);
}
void thirdWay(){
    // Dynamic strings, resizable strings

}

void commonMethods(){
    // strcmp(firstString, secondString):
    // Upon finding the first pair of differing chars, 
    // return the lexicographical difference = first string - second string:
    // Eg. 'h' - 'H' = 32 because lowercase chars are +32 bigger than uppercase chars.
    // Eg. 'H' - 'h' = -32 because uppercase chars are -32 smaller than lowercase chars.
    // Uppercase char are smaller nums, lowercase char are bigger nums
    char* str5 = "Hi";
    char* str6 = "Hi";
    char* str7 = "hi";
    char* str8 = "Hello";
    char* str9 = "HelLo";
    char* str10 = "Hel";
    // printf("Output: %d\n", strcmp(str5, str6)); // returns 0 because no difference
    // printf("Output: %d\n", strcmp(str6, str7)); // returns -32 because H < h
    // printf("Output: %d\n", strcmp(str7, str8)); // returns +32 because h > H
    // printf("Output: %d\n", strcmp(str8, str9)); // returns +32 because l > L
    // printf("Output: %d\n", strcmp(str9, str10)); // returns +76 because L > NULL. L = 76, NULL = 0.

    // strlen(string). Oupts the number of char, including spaces, minus the null terminator.
    // printf("Output: %lu\n",  strlen(str5));

    // strcspn(str1, str2). return length of the initial segment of str1 not containing any characters from str2
    char str1[] = "Hello, world!";
    char str2[] = ",!";
    // Find the length of the initial segment of str1 that does not contain any characters from str2
    int len = strcspn(str1, str2);
    printf("The length of the initial segment of str1 not containing any characters from str2: %d\n", len);

    char str11[] = "Hello, world!";
    str11 += 5;
    printf("str11: %s\n", str11);
}