"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

from collections import deque
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        '''
        Connect each node of a binary tree to its next right node in the same level.

        :param root: The root node of the binary tree.
        :return: The modified binary tree.
        '''
        if not root:
            return None

        que = deque([root])

        while que:
            size = len(que)

            for i in range(size):
                node = que.popleft()

                if node.left:
                    que.append(node.left)

                if node.right:
                    que.append(node.right)

                # Connect the current node to its next right node in the same level
                if i < size - 1:
                    node.next = que[0]

        return root