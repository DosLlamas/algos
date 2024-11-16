#include <stdio.h>
#include <stdlib.h>

int main() {
    /* What are the ways to delcare an array */
    // Here are all the ways you can declare a fixed int array:
    // 0.
    // The [size] is optional if you assign the array upon declaration,
    // but if you include the size, make sure it is not less than the values you gave it.
    int arr0[] = {1, 2, 3}; // Now the max size is the size of assignment you gave. 3 in this case.
    // int arr0[1] = {1, 2, 3}; // This will give an error because the size given is too small to fit the assignment.

    // Be aware of index out of bounds after the size has been set: 
    // arr0[3] = 4; // Index out of bounds error because the max size is already 3.

    // 1.
    // If the declared size is greater than the values given, the rest will be set to 0:
    int arr1[5] = {1, 2}; // The array will be {1, 2, 0, 0, 0}

    // 2.
    // If you don't assign the array upon declaration, size is required.
    int arr2[3]; 
    // But then you cannot reassign arr1 = {1, 2, 3}. You have to assign each index individually or using a loop:
    arr2[0] = 1;
    arr2[1] = 2;
    arr2[2] = 3;
    

    // 3. 
    // The keyword const makes the array immutable:
    const int arr3[] = {1, 2, 3};
    // Now you can't change the index like example 2:
    // arr3[0] = 1; // This still gives an error even though you change the value to the same thing due to const.


    // 4. Better to initialize like this so you don't have garbage values within the array.
    int arr4[20] = {0};

    for(int i = 0; i < (sizeof(arr2) / sizeof(int)); i++){
        printf("%d%s", arr2[i], " ");
    };


    // You cannot declare a fixed array using a pointer variable.
    // But you can reference the fixed array variable using a separate pointer variable
    return 0;
}
