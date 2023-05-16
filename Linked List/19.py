# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        '''
        Remove the N-th node from the end of a linked list.

        :param head: The head of the linked list.
        :param n: The position of the node to be moved.
        :return: The head of the modified linked list.
        '''
        # Create a dummy head to handle the edge case
        dummy_head = ListNode(next=head)
        slow, fast = dummy_head, dummy_head

        # Move the fast pointer n position ahead
        while n >= 0:
            fast = fast.next
            n -= 1

        # Move both pointers until the fast pointer reaches the end
        while fast:
            slow = slow.next
            fast = fast.next

        # Remove the N-th node by updating the next pointer of the slow pointer
        slow.next = slow.next.next

        # Return the head of the modified linked list
        return dummy_head.next