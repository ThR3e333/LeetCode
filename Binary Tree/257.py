# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:

        def backtracking(node):
            path.append(str(node.val))
            if not node.left and not node.right:
                return result.append('->'.join(path))
            if node.left:
                backtracking(node.left)
                path.pop()
            if node.right:
                backtracking(node.right)
                path.pop()

        if not root:
            return []
        path, result = [], []
        backtracking(root)

        return result