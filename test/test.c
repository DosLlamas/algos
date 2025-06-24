#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>

int numLeafNodes(struct treenode* root) {
    if (root == NULL) {
        return 0;
    }
    if (root->left == NULL && root->right == NULL) {
        return 1;
    }
    return numLeafNodes(root->left) + numLeafNodes(root->right);
}

typedef struct node {
    int val;
    struct node* left;
    struct node* right;
} treenode;

typedef struct treenode {
    int val;
    node root;
    struct treenode* left;
    struct treenode* right;
} TreeNode;


int main() {

    treenode* root = malloc(sizeof(treenode));
    root->val = 1; // use pointer because the variable root is a pointer
    treenode roo2;
    roo2.val = 2;

    char** str = malloc(10 * sizeof(char*));
    for (int i = 0; i < 10; i++) {
        str[i] = malloc(100 * sizeof(char));
    }

    char










    int* nums = malloc(3*sizeof(int));
    *(nums+1) = 1;

    printf("%d\n", nums[1]);




    
    return 0;
}