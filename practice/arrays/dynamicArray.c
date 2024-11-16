#include <stdio.h>
#include <stdlib.h>

#define INITIAL_CAPACITY 4 // Initial capacity of the array

// Define the ArrayList structure. 
// You can do this without a struct if you just declare each variable separately and pass all the variables to the functions.
typedef struct {
    int *data;       // Pointer to the array holding the elements
    int size;        // Number of elements currently in the array
    int capacity;    // Capacity of the array
} ArrayList;

// Function to initialize the ArrayList
void initArrayList(ArrayList *list) {
    list->size = 0;
    list->capacity = INITIAL_CAPACITY;
    list->data = (int *)malloc(list->capacity * sizeof(int));
    if (list->data == NULL) {
        printf("Memory allocation failed\n");
        exit(1);
    }
}

// Function to resize the ArrayList when capacity is full
void resizeArrayList(ArrayList *list) {
    list->capacity *= 2; // Double the capacity
    list->data = (int *)realloc(list->data, list->capacity * sizeof(int));
    if (list->data == NULL) {
        printf("Memory reallocation failed\n");
        exit(1);
    }
}

// Function to add an element to the ArrayList at the end
void addElement(ArrayList *list, int value) {
    if (list->size == list->capacity) {
        resizeArrayList(list); // Resize the array if it's full
    }
    list->data[list->size] = value;
    list->size++;
}

// Function to insert an element at a specific index
void insertElement(ArrayList *list, int index, int value) {
    if (index < 0 || index > list->size) {
        printf("Index out of bounds\n");
        return;
    }

    if (list->size == list->capacity) {
        resizeArrayList(list); // Resize the array if it's full
    }

    // Shift elements right to make space for the new element
    for (int i = list->size; i > index; i--) {
        list->data[i] = list->data[i - 1];
    }

    // Insert the new element
    list->data[index] = value;
    list->size++;
}

// Function to get an element from the ArrayList by index
int getElement(ArrayList *list, int index) {
    if (index < 0 || index >= list->size) {
        printf("Index out of bounds\n");
        return -1; // Return a sentinel value for invalid index
    }
    return list->data[index];
}

// Function to remove an element at a specific index
void removeElement(ArrayList *list, int index) {
    if (index < 0 || index >= list->size) {
        printf("Index out of bounds\n");
        return;
    }
    // Shift elements left after the removed element
    for (int i = index; i < list->size - 1; i++) {
        list->data[i] = list->data[i + 1];
    }
    list->size--;
}

// Function to free the memory used by the ArrayList
void freeArrayList(ArrayList *list) {
    free(list->data);
}

// Main function to demonstrate the ArrayList usage
int main() {
    ArrayList list;
    initArrayList(&list); // Initialize the list

    // Add some elements
    addElement(&list, 10);
    addElement(&list, 20);
    addElement(&list, 30);
    addElement(&list, 40);

    printf("List after adding 4 elements:\n");
    for (int i = 0; i < list.size; i++) {
        printf("%d ", getElement(&list, i));
    }
    printf("\n");

    // Insert an element at index 2
    insertElement(&list, 2, 25);

    printf("List after inserting 25 at index 2:\n");
    for (int i = 0; i < list.size; i++) {
        printf("%d ", getElement(&list, i));
    }
    printf("\n");

    // Add more elements to trigger resizing
    addElement(&list, 50);
    addElement(&list, 60);

    printf("List after adding more elements:\n");
    for (int i = 0; i < list.size; i++) {
        printf("%d ", getElement(&list, i));
    }
    printf("\n");

    // Remove an element
    removeElement(&list, 2); // Remove the element at index 2

    printf("List after removing element at index 2:\n");
    for (int i = 0; i < list.size; i++) {
        printf("%d ", getElement(&list, i));
    }
    printf("\n");

    freeArrayList(&list); // Free the dynamically allocated memory

    return 0;
}