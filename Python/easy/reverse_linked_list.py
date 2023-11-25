def reverseList(self, head):
    """
    :type head: ListNode
    :rtype: ListNode

    steps:
    1. 
    declare a left and right pointer
    2.
    iterate loinked list.
    on each iteration,
    save_next_node.
    then reverse node

    3.
    return left_pointer


    Compexity:
    O(n) time | O(1) space
    """

    # left_pointer = None
    # right_pointer = head
    # while right_pointer:
    #     save_next_node = right_pointer.next
    #     right_pointer.next = left_pointer
    #     left_pointer = right_pointer 
    #     right_pointer = save_next_node
    # return left_pointer 

    # Recursive approach
    if not head or not head.next: return head
    final_head = self.reverseList(head.next)
    head.next.next = head
    head.next = None
    return final_head