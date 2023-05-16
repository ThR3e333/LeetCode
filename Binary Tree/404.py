# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        '''
        Calculates the sum of all left leaves in a binary tree.

        :param root: The root node of the binary tree.
        :return: The sum of all left leaves in the binary tree.
        '''
        if not root:
            return 0

        # Calculate the sum of left leaves in the left subtree
        left_left_leaves_sum = self.sumOfLeftLeaves(root.left)

        # Calculate the sum of left leaves in the right subtree
        right_left_leaves_sum = self.sumOfLeftLeaves(root.right)

        # Check if the current node is a left leaf
        cur_left_leaf_val = 0
        if root.left and not root.left.left and not root.left.right:
            cur_left_leaf_val = root.left.val

        return left_left_leaves_sum + right_left_leaves_sum + cur_left_leaf_val