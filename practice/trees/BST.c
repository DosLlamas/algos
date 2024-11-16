#include <stdio.h>
#include <stdlib.h>

// Define the structure of a BST node
struct Node {
    int data;
    struct Node* left;
    struct Node* right;
};

// Function to create a new node in the BST
struct Node* createNode(int data) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = data;
    newNode->left = NULL;
    newNode->right = NULL;
    return newNode;
}

struct Node* insert(struct Node* node, int data) {
    if (node == NULL) {
        return createNode(data);
    }
    if (data < node->data) {
        node->left = insert(node->left, data);
    } else if (data > node->data) {
        node->right = insert(node->right, data);
    }

    return node;
}

struct Node* findMin(struct Node* node) {
    struct Node* current = node;
    while (current && current->left != NULL) current = current->left;
    return current;
}
struct Node* deleteNode(struct Node* root, int key) {
    if (root == NULL) return root;
    if (key < root->data) {
        root->left = deleteNode(root->left, key);
    } else if (key > root->data) {
        root->right = deleteNode(root->right, key);
    } else {
        // Node found
        // Case 1: Node with only one child or no child
        if (root->left == NULL) {
            struct Node* temp = root->right;
            free(root);
            return temp;
        } else if (root->right == NULL) {
            struct Node* temp = root->left;
            free(root);
            return temp;
        }
        // Case 2: Node with two children
        // Get the in-order successor (smallest in the right subtree)
        struct Node* temp = findMin(root->right);
        // Copy the in-order successor's data to this node
        root->data = temp->data;
        // Delete the in-order successor
        root->right = deleteNode(root->right, temp->data);
    }
    return root;
}

void inOrderTraversal(struct Node* root) {
    if (root != NULL) {
        inOrderTraversal(root->left);     // Visit left subtree
        printf("%d ", root->data);        // Print node data
        inOrderTraversal(root->right);    // Visit right subtree
    }
}

struct Node* binarySearch(struct Node* root, int target) {
    // Base case: root is NULL or key is present at root
    if (root == NULL || root->data == target) {
        return root;  // Return the node if found, or NULL if not found
    }
    // target is greater than root's target
    if (target < root->data) {
        return binarySearch(root->left, target);  // Search in the left subtree
    } else {
        return binarySearch(root->right, target); // Search in the right subtree
    }
}
void printSearchResult(struct Node* result, int key) {
    if (result != NULL) {
        printf("Element %d found in the BST.\n", key);
    } else {
        printf("Element %d not found in the BST.\n", key);
    }
}


int main() {
    struct Node* root = NULL;

    // Insert nodes into the BST
    root = insert(root, 50);
    insert(root, 30);
    insert(root, 20);
    insert(root, 40);
    insert(root, 70);
    insert(root, 60);
    insert(root, 80);

    printf("In-Order Traversal of the BST: ");
    inOrderTraversal(root);
    printf("\n");

    int key = 40;
    struct Node* result = binarySearch(root, key);
    printSearchResult(result, key);

     // Delete nodes from the BST
    root = deleteNode(root, 20); // Delete leaf node
    printf("In-Order Traversal after deleting 20: ");
    inOrderTraversal(root);
    printf("\n");

    root = deleteNode(root, 30); // Delete node with one child
    printf("In-Order Traversal after deleting 30: ");
    inOrderTraversal(root);
    printf("\n");

    root = deleteNode(root, 50); // Delete node with two children
    printf("In-Order Traversal after deleting 50: ");
    inOrderTraversal(root);
    printf("\n");

    return 0;
}