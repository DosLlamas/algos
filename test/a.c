#define CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>

int main(){
    int numOfApplesPerBag = 0;
    int numOfBags = 0;
    int costPerDozen = 0;
    scanf("%d%d", &numOfApplesPerBag, &numOfBags);
    scanf("%d", &costPerDozen);

    int numOfApples = numOfApplesPerBag*numOfBags;
    int totalCost = numOfApples%12 == 0 ? costPerDozen*(numOfApples/12) : costPerDozen*(numOfApples/12 + 1);
    printf("%d", totalCost);

    return 0;
}