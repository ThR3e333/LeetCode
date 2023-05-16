"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

from collections import deque
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        '''
        Performs level order traversal of a N-ary tree.

        :param root: The root node of the binary tree.
        :return: A list of lists containing the values of nodes grouped by level.
        '''
        if not root:
            return []

        result = []
        que = deque([root])

        while que:
            # Temporary list to store node values at the current level
            temp = []
            size = len(que)

            # Process all nodes at the same level
            for _ in range(size):
                node = que.popleft()
                temp.append(node.val)

                # Enqueue the children of the current node
                if node.children:
                    que.extend(node.children)

            result.append(temp)

        return result