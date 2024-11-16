#include <stdio.h>

// Only takes numbers from 0 through 255(1 byte or 8 bits)
// The order doesn't matter
void performXOR(unsigned char num1, unsigned char num2);

void performXOR(unsigned char num1, unsigned char num2){
   printf("num1: %d\n", num1);
   printf("num2: %d\n", num2);
   num1 ^= num2;
   printf("Final result after XOR: %d\n", num1);
}

int main(){
    /* 
    1. Take a variable, num, which is 8 bits, and convert it to binary:
        unsigned char num = 5; // 5 in binary is  00000101
    2. Take another variable, num2, which is 8 bits, and convert that to binary:
        unsigned char num2 = 3; // 3 in binary is 00000011
    
    3. Compare the bits, one by one(Right to Left):
        a. 1 vs 1 results in 0 because both bits are 1.
        b. 0 vs 1 results in 1 because only one of the bits is 1.
        b. 1 vs 0 results in 1 because only one of the bits is 1.
        c. The rest of the 5 bits result in 0 because both bits are 0 for each.
        d. The resulting binary number is 00000110, which is 6.
    */
   performXOR(5, 3);
   return 0;
}