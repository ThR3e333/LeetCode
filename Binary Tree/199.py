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
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        '''
        Returns the right side view of a binary tree.

        :param root: The root node of the binary tree.
        :return: A list integers representing the right side view of the binary tree.
        '''
        if not root:
            return []

        result = []
        que = deque([root])

        while que:
            size = len(que)

            # Add the rightmost node value to the result list
            result.append(que[-1].val)

            for _ in range(size):
                node = que.popleft()

                # Add left child to the queue, if it exists
                if node.left:
                    que.append(node.left)

                # Add right child to the queue, if it exists
                if node.right:
                    que.append(node.right)

        return result