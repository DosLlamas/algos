#include <stdio.h>
#include <stdlib.h>

// Define the structure of a binary tree node
struct Node {
    int data;
    struct Node* left;
    struct Node* right;
};

// Function to create a new node
struct Node* createNode(int data) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = data;
    newNode->left = NULL;
    newNode->right = NULL;
    return newNode;
}

// Pre-order DFS: Visit root, left subtree, then right subtree
void preOrderTraversal(struct Node* root) {
    if (root != NULL) {
        printf("%d ", root->data);          // Process the current node
        preOrderTraversal(root->left);      // Visit the left subtree
        preOrderTraversal(root->right);     // Visit the right subtree
    }
}

// In-order DFS: Visit left subtree, root, then right subtree
void inOrderTraversal(struct Node* root) {
    if (root != NULL) {
        inOrderTraversal(root->left);       // Visit the left subtree
        printf("%d ", root->data);          // Process the current node
        inOrderTraversal(root->right);      // Visit the right subtree
    }
}

// Post-order DFS: Visit left subtree, right subtree, then root
void postOrderTraversal(struct Node* root) {
    if (root != NULL) {
        postOrderTraversal(root->left);     // Visit the left subtree
        postOrderTraversal(root->right);    // Visit the right subtree
        printf("%d ", root->data);          // Process the current node
    }
}


struct QueueNode {
    struct Node* treeNode;
    struct QueueNode* next;
};
struct Queue {
    struct QueueNode* front;
    struct QueueNode* rear;
};
struct Queue* createQueue() {
    struct Queue* queue = (struct Queue*)malloc(sizeof(struct Queue));
    queue->front = queue->rear = NULL;
    return queue;
}
void enqueue(struct Queue* queue, struct Node* treeNode) {
    struct QueueNode* newNode = (struct QueueNode*)malloc(sizeof(struct QueueNode));
    newNode->treeNode = treeNode;
    newNode->next = NULL;
    if (queue->rear == NULL) {
        queue->front = queue->rear = newNode;
        return;
    }
    queue->rear->next = newNode;
    queue->rear = newNode;
}
struct Node* dequeue(struct Queue* queue) {
    if (queue->front == NULL)
        return NULL;
    struct QueueNode* temp = queue->front;
    struct Node* treeNode = temp->treeNode;
    queue->front = queue->front->next;
    if (queue->front == NULL)
        queue->rear = NULL;
    free(temp);
    return treeNode;
}
int isQueueEmpty(struct Queue* queue) {
    return queue->front == NULL;
}
void bfsTraversal(struct Node* root) {
    if (root == NULL) return;
    struct Queue* queue = createQueue();
    enqueue(queue, root);
    while (!isQueueEmpty(queue)) {
        struct Node* currentNode = dequeue(queue);
        printf("%d ", currentNode->data);
        if (currentNode->left != NULL)
            enqueue(queue, currentNode->left);
        if (currentNode->right != NULL)
            enqueue(queue, currentNode->right);
    }
    free(queue);  // Clean up the queue
}

int calculateHeight(struct Node* node) {
    if (node == NULL) {
        return -1;  // Return -1 for height convention (number of edges)
    }
    int leftHeight = calculateHeight(node->left);
    int rightHeight = calculateHeight(node->right);

    return 1 + (leftHeight > rightHeight ? leftHeight : rightHeight);
}

int calculateDepth(struct Node* root, struct Node* node, int depth) {
    if (root == NULL) {
        return -1;  // Node not found in the tree
    }
    if (root == node) {
        return depth;
    }

    // Search for the node in the left and right subtrees
    int leftDepth = calculateDepth(root->left, node, depth + 1);
    if (leftDepth != -1) {
        return leftDepth;
    }

    return calculateDepth(root->right, node, depth + 1);
}


int main() {
    // Create a sample binary tree
    struct Node* root = createNode(1);
    root->left = createNode(2);
    root->right = createNode(3);
    root->left->left = createNode(4);
    root->left->right = createNode(5);
    root->right->left = createNode(6);
    root->right->right = createNode(7);

    // Perform DFS traversals
    printf("Pre-Order Traversal: ");
    preOrderTraversal(root);
    printf("\n");

    printf("In-Order Traversal: ");
    inOrderTraversal(root);
    printf("\n");

    printf("Post-Order Traversal: ");
    postOrderTraversal(root);
    printf("\n");

    printf("BFS (Level-Order Traversal) of the Binary Tree: ");
    bfsTraversal(root);
    printf("\n");

    return 0;
}