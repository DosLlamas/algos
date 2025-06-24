#include <stdio.h>

void selectionSort(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        int curr_min = i;
        for (int j = i + 1; j < n; j++) {
            if (arr[j] < arr[curr_min]) {
                curr_min = j;
            }
        }
        if (curr_min != i) {
            int temp = arr[i];
            arr[i] = arr[curr_min];
            arr[curr_min] = temp;
        }
    }
}
void insertionSort(int arr[], int n) {
    for (int i = 1; i < n; i++) {
        int current = arr[i];  
        int j = i - 1;
        while (j >= 0 && arr[j] > current) {
            arr[j + 1] = arr[j];
            j = j - 1;
        }
        arr[j + 1] = current;
    }
}
void bubbleSort(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        int swapped = 0; // Flag to check if any swapping occurred in this pass
        // Last i elements are already in place, so loop until n - i - 1
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
                swapped = 1;  // Set flag to indicate a swap occurred
            }
        }
        // If no two elements were swapped in this pass, the array is sorted
        if (swapped == 0) {
            break;
        }
    }
}
void merge(int* arr, int l, int mid, int r) {
    int n1 = mid - l + 1;  // Size of left subarray
    int n2 = r - mid;      // Size of right subarray
    int left[n1], right[n2];
    // Copy data to temporary arrays left[] and right[]
    for (int i = 0; i < n1; i++)
        left[i] = arr[l + i];
    for (int i = 0; i < n2; i++)
        right[i] = arr[mid + 1 + i];
    int i = 0;
    int j = 0;
    int k = l;
    while (i < n1 && j < n2) {
        if (left[i] <= right[j]) {
            arr[k] = left[i]; // Left first so it's stable
            i++;
        } else {
            arr[k] = right[j];
            j++;
        }
        k++;
    }
    // Copy the remaining elements of left[], if any
    while (i < n1) {
        arr[k] = left[i];
        i++;
        k++;
    }
    // Copy the remaining elements of right[], if any
    while (j < n2) {
        arr[k] = right[j];
        j++;
        k++;
    }
}
void mergeSort(int arr[], int left, int right) {
    if (left < right) {
        // Same as (left+right)/2, but avoids int overflow for big numbers
        int mid = left + (right - left) / 2;
        // Sort first and second halves
        mergeSort(arr, left, mid);
        mergeSort(arr, mid + 1, right);
        // Merge the halves
        merge(arr, left, mid, right);
    }
}

#define THRESHOLD 10  // Set the threshold for switching to insertion sort

void insertSort(int arr[], int left, int right) {
    for (int i = left + 1; i <= right; i++) {
        int key = arr[i];
        int j = i - 1;
        while (j >= left && arr[j] > key) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = key;
    }
}

void mergeInsertSort(int arr[], int left, int right) {
    if (right - left + 1 <= THRESHOLD) {
        // Use insertion sort for small subarrays
        insertSort(arr, left, right);
    } else {
        int mid = left + (right - left) / 2;
        
        // Recursively sort each half
        mergeInsertSort(arr, left, mid);
        mergeInsertSort(arr, mid + 1, right);

        // Merge the sorted halves
        merge(arr, left, mid, right);
    }
}
void swap(int* a, int* b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}
// First element as pivot using two while loops
int partitionFirst(int arr[], int low, int high) {
    int pivot = arr[low]; // Pivot
    int i = low + 1;      // Index of smaller element
    int j = high;         // Index of larger element
    while (i <= j) {
        while (i <= high && arr[i] <= pivot) i++;
        while (j >= low && arr[j] > pivot) j--;
        if (i < j) 
            swap(&arr[i], &arr[j]);
        else break;
    }
    swap(&arr[low], &arr[j]); // Put pivot in correct position
    return j; // Return pivot index
}
// Middle element as pivot
int partitionMiddle(int arr[], int low, int high) {
    int pivot = arr[low + (high - low) / 2]; // Pivot
    int i = low - 1;      // Index of smaller element
    int j = high + 1;     // Index of larger element
    while (1) {
        do {
            i++;
        } while (arr[i] < pivot);
        do {
            j--;
        } while (arr[j] > pivot);
        if (i >= j) {
            return j;
        }
        swap(&arr[i], &arr[j]);
    }
}
// Last element as pivot using two while loops
int partitionLast(int arr[], int low, int high) {
    int pivot = arr[high]; // Pivot
    int i = low - 1;       // Index of smaller element
    for (int j = low; j < high; j++) {
        if (arr[j] < pivot) {
            i++;
            swap(&arr[i], &arr[j]);
        }
    }
    swap(&arr[i + 1], &arr[high]); // Put pivot in correct position
    return i + 1; // Return pivot index
}

void quickSort(int arr[], int low, int high) {
    if (low < high) {
        int pi = partitionMiddle(arr, low, high);
        // Recursively apply quicksort to each partition
        quickSort(arr, low, pi - 1);  
        quickSort(arr, pi + 1, high);
    }
}

void printArray(int arr[], int size) {
    int i;
    for (i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

int main() {
    int arr[] = {64, 25, 12, 22, 11};
    int length = sizeof(arr) / sizeof(arr[0]);
    printf("Original array: ");
    printArray(arr, length);

    printf("Selection Sorted array: ");
    selectionSort(arr, length);
    printArray(arr, length);

    printf("Insertion Sorted array: ");
    insertionSort(arr, length);
    printArray(arr, length);

    printf("Bubble Sorted array: ");
    bubbleSort(arr, length);
    printArray(arr, length);

    printf("Merge Sorted array: ");
    mergeSort(arr, 0, length - 1);
    printArray(arr, length);

    printf("Merge-Insert Sorted array: ");
    mergeInsertSort(arr, 0, length - 1);
    printArray(arr, length);

    printf("Quick Sorted array: ");
    quickSort(arr, 0, length - 1);
    printArray(arr, length);
    return 0;
}