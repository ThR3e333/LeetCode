# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        '''
        Determine if a binary tree is balanced.

        :param root: The root of the binary tree.
        :return: True if the binary tree is balanced, False otherwise.
        '''
        def getHeight(node):
            # Base case: If node is None, return 0
            if not node:
                return 0

            # Recursively calculate the heights of left and right subtrees
            left_height = getHeight(node.left)
            if left_height == -1:
                return -1

            right_height = getHeight(node.right)
            if right_height == -1:
                return -1

            # Check if the heights of the subtrees differ by more than one
            if abs(left_height - right_height) > 1:
                return -1

            # Calculate the height of the current node
            else:
                height = 1 + max(left_height, right_height)

            return height

        return getHeight(root) != -1