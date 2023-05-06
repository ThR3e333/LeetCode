# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
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
            return []
        path, result = [], []
        backtracking(root, targetSum)
        return result