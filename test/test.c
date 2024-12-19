#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>

typedef struct Node {
    char symbol;
    struct Node* next;
} Node;

typedef struct Stack {
    Node* top;
} Stack;

Node* createNode(char symbol) {
    Node* newNode = (Node*)malloc(sizeof(Node));
    newNode->symbol = symbol;
    newNode->next = NULL;
    return newNode;
}

void freeStack(Stack* stack) {
    Node* curr = stack->top;
    while (curr) {
        Node* temp = curr;
        curr = curr->next;
        free(temp);
    }
}

void push(Stack* stack, char symbol) {
    Node* newNode = createNode(symbol);
    newNode->next = stack->top;
    stack->top = newNode;
}

unsigned char isEmpty(Stack* stack) {
    return stack->top == NULL;
}

char pop(Stack* stack) {
    if (isEmpty(stack)) {
        printf("Empty stack\n");
        return -1;
    } else {
        char symbol = stack->top->symbol;
        Node* temp = stack->top;
        stack->top = stack->top->next;
        free(temp);
        return symbol;
    }
}

char peek(Stack* stack) {
    if (isEmpty(stack)) {
        return -1;
    }
    else{
        return stack->top->symbol;
    }
}

// Function to check precedence of operators
int precedence(char op) {
    if (op == '+' || op == '-') {
        return 1;
    }
    if (op == '*' || op == '/') {
        return 2;
    }
    if (op == '^') {
        return 3;
    }
    return 0;
}

// Function to check if a character is an operator
int isOperator(char ch) {
    return ch == '+' || ch == '-' || ch == '*' || ch == '/' || ch == '^';
}

// Convert infix to postfix
void infixToPostfix(Stack* stack, char* infix, char* postfix) {
    int j = 0; // Index for postfix array
    for (int i = 0; infix[i] != '\0'; i++) {
        char ch = infix[i];

        // If operand, add to postfix expression
        if (isalnum(ch)) {
            postfix[j++] = ch;
        }
        // If '(', push to stack
        else if (ch == '(') {
            push(stack, ch);
        }
        // If ')', pop and output until '(' is encountered
        else if (ch == ')') {
            while (!isEmpty(stack) && peek(stack) != '(') {
                postfix[j++] = pop(stack);
            }
            pop(stack); // Pop '('
        }
        // If operator, handle precedence
        else if (isOperator(ch)) {
            while (!isEmpty(stack) && precedence(peek(stack)) >= precedence(ch)) {
                postfix[j++] = pop(stack);
            }
            push(stack, ch);
        }
    }

    // Pop all remaining operators from the stack
    while (!isEmpty(stack)) {
        postfix[j++] = pop(stack);
    }
    postfix[j] = '\0'; // Null-terminate the postfix expression
    freeStack(stack);
}

int main() {
    Stack myStack;
    myStack.top = NULL;
    char infix[100], postfix[100];
    printf("Enter infix expression: ");
    scanf("%s", infix);
    infixToPostfix(&myStack, infix, postfix);
    printf("Postfix expression: %s\n", postfix);

    return 0;
}