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
        if not root:
            return True
        def helper(left, right):
            if not left and right:
                return False
            elif left and not right:
                return False
            elif not left and not right:
                return True
            elif left.val != right.val:
                return False
            outside = helper(left.left, right.right)
            inside = helper(left.right, right.left)
            result = outside and inside
            return result

        return helper(root.left, root.right)
