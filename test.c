#include <stdio.h>

int main() {
    // char* input = "";
    // // input = "hi";
    // scanf("%s", input);
    // printf("%s\n", input);
    // short num = 1;
    // printf("%d\n", num);
    int num = 10;
    int num2 = num;
    printf("%p\n", &num);
    printf("%p\n", &num2);
    return 0;
}