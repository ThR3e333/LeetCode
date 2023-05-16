# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Swap pairs of nodes in a linked list.

        :param head: The head of the linked list.
        :return: The head of the modified linked list.
        '''
        # Create a dummy head to handle the edge case
        dummy_head = ListNode(next=head)

        # Initialize the left node as the dummy head
        left_node = dummy_head

        while left_node.next and left_node.next.next:
            # Get references to the middle and right nodes
            middle_node = left_node.next
            right_node = left_node.next.next

            # Swap the middle and right nodes
            middle_node.next = right_node.next
            right_node.next = middle_node
            left_node.next = right_node

            # Move the left node two steps forward
            left_node = left_node.next.next

        # Return the head of the modified linked list
        return dummy_head.next