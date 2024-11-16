#include <stdio.h>
#include <stdlib.h>

// // Definition of the Node structure
// typedef struct Node {
//     int value;
//     struct Node* next;
// } Node;

// // Recursive function to remove the tail of the linked list
// Node* removeTail(Node* head) {
//     // Base case: If the list is empty or has only one node
//     if (head == NULL) return NULL;
    
//     if(head->next == NULL){
//           free(head);
//           return NULL;
//     }
    
//     // Recursive case: Check if we're at the second-to-last node
//     if (head->next->next == NULL) {
//         // Free the tail node and set the next pointer to NULL
//         free(head->next);
//         head->next = NULL;
//         return head;
//     }

//     // Recursively call the function to go deeper into the list
//     head->next = removeTail(head->next);
    
//     // Return the head node to preserve the list
//     return head;
// }

// // Helper function to create a new node
// Node* createNode(int value) {
//     Node* newNode = (Node*)malloc(sizeof(Node));
//     newNode->value = value;
//     newNode->next = NULL;
//     return newNode;
// }

// // Helper function to print the list
// void printList(Node* head) {
//     while (head != NULL) {
//         printf("%d -> ", head->value);
//         head = head->next;
//     }
//     printf("NULL\n");
// }

// int main() {
//     // Node* head = NULL;
//     Node* head = createNode(1);
//     head->next = createNode(2);
//     head->next->next = createNode(3);
//     head->next->next->next = createNode(4);
//     head->next->next->next->next = createNode(5);

//     printf("Original list: ");
//     printList(head);

//     // Remove the tail
//     head = removeTail(head);

//     printf("List after removing the tail: ");
//     printList(head);

//     // Clean up the remaining list
//     while (head != NULL) {
//         Node* temp = head;
//         head = head->next;
//         free(temp);
//     }

//     return 0;
// }

// int recursiveSum(int *array, int size) {
//     if (size <= 0) return 0;  // Base case: no elements to sum
//     return array[size - 1] + recursiveSum(array, size - 1);  // Add last element and recursiveSum
// }
// int fac(int n){
//     if (n == 0) return 1;
//     else return n * fac(n - 1);
// }
// int fact(int n){
//     if (n <= 1) return 1;
//     return n * fact(n - 1);
// }
// int main(){
//     // int arr[] = {1, 2, 3, 4, 10};
//     // int size = sizeof(arr)/sizeof(arr[0]);
//     // printf("%d\n", recursiveSum(arr, size));
//     printf("%d\n", fac(6));
//     return 0;
// }

// Towers of Hanoi: 3 towers
// void towers(int n, int start, int end) {
//     if (n > 0) {
//         int mid = 6 - start - end;
//         towers(n-1, start, mid);
//         printf("Move disk %d from tower ", n);
//         printf("%d to tower %d.\n", start, end);
//         towers(n-1, mid,end);
//     }
// }

// int main() {
//     towers(3, 1, 3);
//     return 0;
// }

// Towers of Hanoi: 4 towers 

// int findMax(int* arr, int max, int index){
//     if(index == 0) return max;
//     if(arr[index] > max) max = arr[index];
//     return findMax(arr, max, index - 1);
// }


// int main(){
//     int arr[] = {1, 7, 5, 9, 12, 3, 0, 14, 6, 2};
//     int size = sizeof(arr)/sizeof(arr[0]);
//     printf("%d\n", findMax(arr, arr[size - 1], size - 1));
//     return 0;
// }

