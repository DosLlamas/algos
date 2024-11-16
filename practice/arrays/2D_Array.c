#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(){

    // 2 ways to declare due to strings:
    // 1st way, fixed size multi-dimensional arrays:
    // The size for rows is optional but size for columns is required.
    int arr0[][4] = { // I don't have to put a size in the first brackets for rows as it will implicitly get the size.
        {1, 2, 3, 4},
        {5, 6, 7, 8},
        {9, 10, 11, 12}
    };
    int arr1[10][10] = {0}; // The 10 rows and columns will be set to 0
    // printf("%d", arr1[9][9]);

    // Array of Strings, rows is not required but the lengh of each string is.
    char arrOfStrings0[][2] = {"Hi", "hi", "By"};

    // Array of Strings with Variable Length Strings using a pointer. Initial size not required.
    char* arr2[3] = {"Hi", "Banana", "Tower"};

    // Table of strings. Rows still not required but num of columns and length of each string is.
    char tableOfStrings[][2][2] = {
        "hi", "hi",
        "hi", "hi",
        "By", "No"
    };

    // 2nd way, dynamic size multi-dimensional arrays:
    // Dynamic size Table of numbers:
    int** arr3;
    arr3 = (int**)malloc(3 * sizeof(int*));  // Allocating memory for 3 rows
    for (int i = 0; i < 3; i++) {
        arr3[i] = (int*)malloc(4 * sizeof(int));  // Allocating memory for 4 columns in each row
    }

    // Dynamic Array of Strings:
    char** arr4 = (char**)malloc(3 * sizeof(char*));  // Allocate memory for 3 strings
    for (int i = 0; i < 3; i++) {
        arr4[i] = (char*)malloc(20 * sizeof(char));  // Allocate memory for each string to hold 20 characters
    }

    // Dynamic Table of Strings:
    int rows = 2;  // Number of rows 
    int columns = 3;    // Number of columns
    int max_len = 50; // Maximum length of each string (3rd dimension)

    // Step 1: Allocate memory for rows (array of pointers to 2D arrays)
    char ***table = (char ***)malloc(rows * sizeof(char **));
    if (table == NULL) {
        printf("Memory allocation for rows failed!\n");
        return 1;
    }

    // Step 2: Allocate memory for columns in each row
    for (int i = 0; i < rows; i++) {
        table[i] = (char **)malloc(columns * sizeof(char *));
        if (table[i] == NULL) {
            printf("Memory allocation for rows in layer %d failed!\n", i);
            return 1;
        }

        // Step 3: Allocate memory for each string in the current row
        for (int j = 0; j < columns; j++) {
            table[i][j] = (char *)malloc(max_len * sizeof(char));
            if (table[i][j] == NULL) {
                printf("Memory allocation for string in layer %d, row %d failed!\n", i, j);
                return 1;
            }
        }
    }
    // Step 4: Fill the 3D array with strings
    strcpy(table[0][0], "Row 0, Column 0: Hello!");
    strcpy(table[0][1], "Row 0, Column 1: Dynamic");
    strcpy(table[0][2], "Row 0, Column 2: Memory Allocation");

    strcpy(table[1][0], "Row 1, Column 0: C Programming");
    strcpy(table[1][1], "Row 1, Column 1: 3D Arrays");
    strcpy(table[1][2], "Row 1, Column 2: Example");

    // Step 5: Print the 3D array
    printf("Dynamic 3D Array of Strings:\n");
    for (int i = 0; i < rows; i++) {
        // printf("Row %d:\n", i);
        for (int j = 0; j < columns; j++) {
            printf("  %s\n", table[i][j]);
        }
    }

    // Step 6: Free the allocated memory
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < columns; j++) {
            free(table[i][j]);  // Free memory for each string
        }
        free(table[i]);  // Free memory for each row
    }
    free(table);  // Free memory for layers
    return 0;
}