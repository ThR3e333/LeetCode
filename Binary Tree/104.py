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
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        '''
        Returns the maximum depth of a binary tree.

        :param root: The root node of the tree.
        :return: The maximum depth of the tree.
        '''
        # Recursively get the maximum depth of the tree
        def getDepth(node, current_depth):

            # Update the maximum depth if needed
            nonlocal max_depth
            max_depth = max(max_depth, current_depth)

            # Recuse on left and right children
            if not node.left and not node.right:
                return
            if node.left:
                getDepth(node.left, current_depth + 1)
            if node.right:
                getDepth(node.right, current_depth + 1)

        # Base case: empty tree
        if not root:
            return 0

        # Initialize the maximum depth to 0 and start recursion
        max_depth = 0
        getDepth(root, 0)

        # The maximum depth is the length of the longest path from the root to a leaf node
        return max_depth + 1

# Approach 2
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        '''
        Returns the maximum depth of a binary tree.

        :param root: The root node of the tree.
        :return: The maximum depth of the tree.
        '''
        def get_depth(current_node):
            '''
            Recursively calculate the depth of the given node.
            :param root:
            :return:
            '''

            # Base case: empty node
            if not current_node:
                return 0

            # Recursively calculate the depth of the left and right children
            left_depth = get_depth(current_node.left)
            right_depth = get_depth(current_node.right)

            # The depth of the current node is 1 plus the maximum depth of its children
            depth = 1 + max(left_depth, right_depth)
            return depth

        return get_depth(root)

# Approach 3

from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        '''
        Returns the maximum depth of a binary tree.
        :param root: The root of the tree.
        :return: The maximum depth of the tree.
        '''

        # Base case: empty tree
        if not root:
            return 0

        depth = 0
        queue = deque([root])

        while queue:
            # Process all nodes at the current level
            level_size = len(queue)
            for _ in range(level_size):
                node = queue.popleft()

                # Add the left and right children of the current node to the queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # Increment the depth for the next level
            depth += 1

        return depth