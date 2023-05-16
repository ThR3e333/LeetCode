'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
'''

from collections import deque
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        '''
        Finds the largest value in each row of a binary tree.

        :param root: The root node of the binary tree.
        :return: A list of the largest value in each row.
        '''
        if not root:
            return []

        result = []
        que = deque([root])

        while que:
            # Temporary list to store the values of nodes in the current level
            temp = []
            size = len(que)

            # Process all nodes at the same level
            for _ in range(size):
                node = que.popleft()
                temp.append(node.val)

                # Enqueue the left and right child nodes, if they exist
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)

            result.append(max(temp))

        return result