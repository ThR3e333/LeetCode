'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
'''

# Approach 1

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        '''
        Find the minimum depth of a binary tree.

        :param root: The root node of the binary tree.
        :return: The minimum depth of the binary tree.
        '''
        def getDepth(root, current_depth):
            nonlocal min_depth

            # If the current node is a leaf node, update the minimum depth if necessary
            if not root.left and not root.right:
                min_depth = min(min_depth, current_depth)
                return

            # Recursively traverse the left and right subtrees
            if root.left:
                getDepth(root.left, current_depth + 1)
            if root.right:
                getDepth(root.right, current_depth + 1)

        if not root:
            return 0

        min_depth = float('inf')
        getDepth(root, 1)

        return min_depth

# Approach 2

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        '''
        Find the minimum depth of a binary tree.

        :param root: The root node of the binary tree.
        :return: The minimum depth of the binary tree.
        '''

        if not root:
            return 0

        # Base case: if the current node is a leaf node, return 1
        if not root.left and not root.right:
            return 1

        min_depth = float('inf')

        # If the left child exists, recursively calculate the minimum depth
        if root.left:
            min_depth = min(self.minDepth(root.left), min_depth)

        # If the right child exists, recursively calculate the minimum depth
        if root.right:
            min_depth = min(self.minDepth(root.right), min_depth)

        return min_depth+1

# Approach 3

from collections import deque
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        '''
        Find the minimum depth of a binary tree.

        :param root: The root node of the binary tree.
        :return: The minimum depth of the binary tree.
        '''
        if not root:
            return 0

        # Create a queue to perform level order traversal
        que = deque([root])
        min_depth = 0

        while que:
            # Get the number of nodes at the current level
            size = len(que)
            min_depth += 1

            # Process each node at the current level
            for _ in range(size):
                node = que.popleft()

                # Add the left child to the queue if it exists
                if node.left:
                    que.append(node.left)

                # Add the right child to the queue if it exists
                if node.right:
                    que.append(node.right)

                # If the current node is a leaf node, return the depth
                if not node.left and not node.right:

                    return min_depth