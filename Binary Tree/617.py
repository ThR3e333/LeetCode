# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        '''
        Merges two binary trees by summing up the corresponding nodes.
        :param root1:
        :param root2:
        :return:
        '''
        # If root1 is empty, return root2
        if not root1:
            return root2

        # If root2 is empty, return root1
        if not root2:
            return root1

        # Update the value of root1 by summing it with root2
        root1.val += root2.val

        # Recursively merge the left subtrees of root1 and root2
        root1.left = self.mergeTrees(root1.left, root2.left)

        # Recursively merge the right subtrees of root1 and root2
        root1.right = self.mergeTrees(root1.right, root2.right)

        return root1