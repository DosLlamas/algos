'''
You're given the head of a Singly Linked List whose nodes are in sorted order
with respect to their values. Write a function that returns a modified version
of the Linked List that doesn't contain any nodes with duplicate values. The
Linked List should be modified in place (i.e., you shouldn't create a brand
new list), and the modified Linked List should still have its nodes sorted
with respect to their values

Each "LinkedList" node has an integer value as well as a "next" node pointing to 
the next node in the list or to "None/null" if it's the tail of the list.

Sample Input
linkedList = 1 -> 1 -> 3 -> 4 -> 4 -> 4 -> 5 -> 6 -> 6 

Sample Output
1 -> 3 -> 4 -> 5 -> 6 

Approach:

Steps:
1.
Check if current node.value equals node.next.value
2.
If yes, current node.value = node.next.next
3.
return result
'''

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# sample_input = LinkedList({1:{1:{3:{4:{4:{4:{5:{6:{6:None}}}}}}}}})
# # print(sample_input)

# def removeDuplicatesFromLinkedList(linkedList):
#     # Write your code here.
#     while linkedList.value == linkedList.next.value:
#         linkedList = linkedList.next.next
    
#     return linkedList

# print(removeDuplicatesFromLinkedList(sample_input))

# I completely failed that first attempt. I believe my idea works 
# but I don't know how to implement this yet
def removeDuplicatesFromLinkedList2(linkedList):
    # Write your code here.
    while linkedList.value == linkedList.next.value:
        linkedList = linkedList.next.next
    
    return linkedList