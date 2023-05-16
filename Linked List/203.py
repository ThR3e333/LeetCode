# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        '''
        Remove all nodes with the given value from the linked list.

        :param head: The head of the linked list.
        :param val: The value to be removed from the linked list.
        :return: The head of the updated linked list.
        '''
        # Create dummy head node to handle the edge case
        dummy_head = ListNode(next=head)

        # Pointer to track the current node
        current_node = dummy_head

        while current_node.next is not None:
            # Remove the node with given value
            if current_node.next.val == val:
                current_node.next = current_node.next.next

            # Move to the next node
            else:
                current_node = current_node.next
        return dummy_head.next