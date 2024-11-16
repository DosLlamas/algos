#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    int arr1[] = {1, 2, 3};
    // int arr2[] = {1, 2, 3};
    printf("%d\n", *((&arr1[0])+1));
    // printf("%p\n", &arr2[0]);
    return 0;
}
