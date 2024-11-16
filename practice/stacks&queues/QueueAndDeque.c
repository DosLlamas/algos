/* 
Goal: Write a function that adds an item to the front/head of the queue. You may use the function makeNode()

Input: Deque and int val
Output: No output, just referencing


Steps:
1.
Make a new node using makeNode()
2.
Check if Deque is empty
3.
check if deque is empty to make the newNode the front and back
4.
If not empty, just add the newNode.



 */
// void addFront(deque* myDeque, int val){
//     node* newNode = makeNode(val);
//     if(myDeque->front == NULL){
//         myDeque->front = newNode;
//         myDeque->back = newNode;
//         return;
//     }
//     newNode->next = myDeque->front;
//     myDeque->front = newNode;
// }