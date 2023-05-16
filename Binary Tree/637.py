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
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        '''
        Calculate the average value of nodes at each level of a binary tree.

        :param root: The root node of the binary tree.
        :return: A list of average values at each level.
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

            # Calculate the average of the current level and append it to the result
            result.append(sum(temp)/size)

        return result