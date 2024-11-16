#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define LEN 100
#define INIT_CAP 2

typedef struct ArrayList ArrayList;

// DONT DO THIS PLEASE!
// #define ArrayList struct ArrayList

struct ArrayList {
    int size, cap;
    char ** names;
};

ArrayList * createList();
void append(ArrayList * list, char * name);
int contains(ArrayList * haystack, char * needle);
void cleanUp(ArrayList * list);

ArrayList * createList() {
    // TODO FIX
    ArrayList * res = (ArrayList *) malloc(sizeof(ArrayList));

    res->size = 0;
    res->cap = INIT_CAP;
    res->names = (char **) malloc(sizeof(char *) * INIT_CAP);

    return res;
}
void append(ArrayList * list, char * name) {
    // Check for fullness
    if (list->size == list->cap) {
        // Expand if full
        list->cap *= 2;

        // realloc takes the old pointer and new memory size
        list->names = (char **) realloc(list->names, list->cap * sizeof(char *));
    }   

    // Add the name into list TODO FIX THIS
    list->names[list->size] = strdup(name);
    list->size++; // WE added a new name to the list
}
int contains(ArrayList * haystack, char * needle) {
    // Linear search throught the full haystack
    for (int i = 0; i < haystack->size; i++) {
        // Check if the i-th has the needle
        if (0 == strcmp(haystack->names[i], needle)) {
            return 1;
        }
    }
    return 0;
}
void cleanUp(ArrayList * list) {
    for (int i = 0; i < list->size; i++) {
        free(list->names[i]);
    }
    free(list->names);
    free(list);
}

void printList(ArrayList * list) {
    for (int i = 0; i < list->size; i++) {
        printf("DEBUG: [%s]\n", list->names[i]);
    }
    printf("\n");
}

int main() {
    ArrayList * list = createList();
    char buffer[LEN + 1];
    scanf("%s", buffer);
    while (0 != strcmp("END", buffer)) {
        append(list, buffer);
        scanf("%s", buffer);
    }

    scanf("%s", buffer);
    printList(list);
    if (contains(list, buffer)) {
        printf("The name %s was in the list.\n", buffer);
    } else {
        printf("The name %s was NOT in the list.\n",
               buffer);
    }

    cleanUp(list);

    return 0;
}
