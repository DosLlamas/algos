#include <stdio.h>

// Function that modifies the value (Pass by value)
// Allocate memory for an int and puts the int given
// into the new memory cell
void passByValue(int x) {
    printf("Memory address of the copy: %p\n", (void*)&x);
    x++;  // Changes only the local copy

}

// Function that modifies the value (Pass by reference)
// Allocate memory for a pointer to an int and puts the
// pointer given into the new memory cell
void passByReference(int *x) {
    // The paranthesis and pointer notation is required
    // to access which memory address the pointer holds
    // Then we increment the value of the original memory cell
    (*x)++;
}

int main() {
    int a = 5;
    // Print what memory address the variable "a" references(De-reference it)
    printf("Memory address of original: %p\n", (void*)&a);

    // In both functions, a new memory address is used. But one stores a
    // copy of the original value while another stores a pointer to the original value.


    // Call by value: the original variable `a` will not be modified
    passByValue(a);
    printf("After pass by value, a = %d\n", a);  // Output: 5

    // Call by reference: the original variable `a` will be modified
    passByReference(&a);
    printf("After pass by reference, a = %d\n", a);  // Output: 6

    return 0;
}