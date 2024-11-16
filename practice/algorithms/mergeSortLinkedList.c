#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node* next;
};

// Function to merge two sorted linked lists
struct Node* sortedMerge(struct Node* a, struct Node* b) {
    struct Node* result = NULL;

    // Base cases
    if (a == NULL)
        return b;
    if (b == NULL)
        return a;

    // Pick either a or b and recur
    if (a->data <= b->data) {
        result = a;
        result->next = sortedMerge(a->next, b);
    } else {
        result = b;
        result->next = sortedMerge(a, b->next);
    }
    return result;
}

// Function to split the linked list into two halves
void frontBackSplit(struct Node* source, struct Node** frontRef, struct Node** backRef) {
    struct Node* slow;
    struct Node* fast;
    slow = source;
    fast = source->next;

    // Advance 'fast' two nodes, and 'slow' one node
    while (fast != NULL) {
        fast = fast->next;
        if (fast != NULL) {
            slow = slow->next;
            fast = fast->next;
        }
    }

    // 'slow' is before the midpoint in the list, so split it in two at that point
    *frontRef = source;
    *backRef = slow->next;
    slow->next = NULL;
}

// Merge Sort function for linked list
void mergeSort(struct Node** headRef) {
    struct Node* head = *headRef;
    struct Node* a;
    struct Node* b;

    // Base case -- length 0 or 1
    if ((head == NULL) || (head->next == NULL)) {
        return;
    }

    // Split head into 'a' and 'b' sublists
    frontBackSplit(head, &a, &b);

    // Recursively sort the sublists
    mergeSort(&a);
    mergeSort(&b);

    // Merge the two sorted lists together
    *headRef = sortedMerge(a, b);
}

// Helper function to insert a new node at the beginning
void push(struct Node** headRef, int new_data) {
    struct Node* new_node = (struct Node*)malloc(sizeof(struct Node));
    new_node->data = new_data;
    new_node->next = *headRef;
    *headRef = new_node;
}

// Helper function to print the linked list
void printList(struct Node* node) {
    while (node != NULL) {
        printf("%d ", node->data);
        node = node->next;
    }
    printf("\n");
}

int main() {
    struct Node* head = NULL;

    // Creating an unsorted linked list
    push(&head, 15);
    push(&head, 10);
    push(&head, 5);
    push(&head, 20);
    push(&head, 3);
    push(&head, 2);

    printf("Original Linked List: \n");
    printList(head);

    // Sort the linked list
    mergeSort(&head);

    printf("Sorted Linked List: \n");
    printList(head);

    return 0;
}