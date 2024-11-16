#include <stdio.h>
#include <stdlib.h>

// Ways to use typedef with Node as example:

// 1st way, declare alias at beginning:
// Ways to use typedef with Node as example:


typedef struct Node{
    int value;
    struct Node *next; // "struct" required here because alias was not declared at beginning
} Node;

int main(){
    // Create a Node instance
    // Node node;
    // Node node2;

    // // Set the data members.
    // node.value = 0;
    // node.next = NULL;

    // node2.value = 1;
    // node2.next = &node;

    // printf("%d", ((double)2)/2.1);
    return 0;
}