# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def backtracking(node, targetSum):
            path.append(node.val)
            if not node.left and not node.right and sum(path) == targetSum:
                result.append(path[:])
            if node.left:
                backtracking(node.left, targetSum)
                path.pop()
            if node.right:
                backtracking(node.right, targetSum)
                path.pop()

        if not root:
            return False
        path, result = [], []
        backtracking(root, targetSum)
        return True if result != [] else False