#include <stdio.h>

static int test = 0;

int testStatic(){
    test = 1;
    return test;
}

int main(){
    testStatic();
    return 0;
}