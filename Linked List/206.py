# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Reverse a linked list.

        :param head: The head of the lined list.
        :return: The head of the reversed list.
        '''
        previous_node, current_node = None, head

        while current_node:
            # Store the reference to the next node
            temp = current_node.next

            # Reverse the link to the previous node
            current_node.next = previous_node

            # Move to the next nodes
            previous_node, current_node = current_node, temp

        # Return the new head of the reversed linked list
        return previous_node