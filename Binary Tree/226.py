'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        '''
        Inverts a binary tree by swapping the left and right children of each node.

        :param root: The root of the binary tree.
        :return: The root node of the inverted binary tree.
        '''
        # If the root is not None, perform tree inversion
        if root:
            # Swap the left and right children of the current node
            root.left, root.right = root.right, root.left

            # Recursively invert the left subtree
            self.invertTree(root.left)

            # Recursively invert the right subtree
            self.invertTree(root.right)

            return root

        # If the root is None, return None
        return None

