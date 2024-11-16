#include <stdio.h>

int binSearchRec(int *values, int low, int high, int searchval) {
    if (low <= high) {
        int mid = low + (high - low) / 2;
        if (searchval < values[mid]){
            return binSearchRec(values, low, mid-1, searchval);
        }
        else if (searchval > values[mid]){
            return binSearchRec(values, mid+1, high, searchval);
        }
        else{ 
            return mid;
        };
    }
    return -1;
}

int binSearchIt(int* array, int size, int val){
    int left = 0;
    int right = size - 1;
    while(left <= right){
        int mid = left + (right - left) / 2;
        if(val < array[mid]){
            right = mid - 1;
        }
        else if(val > array[mid]){
            left = mid + 1;
        }
        else {
            return mid;
        }
    }
    return -1;
}

int main(){
    int arr[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int len  = (sizeof(arr) / sizeof(arr[0]));
    int* ptr = arr;
    // printf("%d\n", binSearchRec(ptr, 0, 9, 6));
    printf("%d\n", binSearchIt(ptr, len, 10));
    return 0;
}