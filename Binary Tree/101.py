'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
'''

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        '''
        Determine if a binary tree is symmetric.

        :param root: The root node of the binary tree.
        :return: True if the tree is symmetric, False otherwise.
        '''
        if not root:
            return True

        def helper(left, right):
            '''
            Recursively check if the subtrees rooted at 'left' and 'right' are symmetric.

            :param left: The root node of the left subtree.
            :param right: The root node of the right subtree.
            :return: True if the subtrees are symmetric, False otherwise.
            '''
            # If both subtrees are empty, then they are symmetric
            if not left and not right:
                return True

            # If only one subtree is empty, then they are not symmetric
            elif not left or not right:
                return False

            # If the values of the nodes are different, then they are not symmetric
            elif left.val != right.val:
                return False

            # Recursively check if the subtrees are symmetric
            outside = helper(left.left, right.right)
            inside = helper(left.right, right.left)

            # If both subtrees are symmetric, the entire tree is symmetric
            return outside and inside

        return helper(root.left, root.right)
