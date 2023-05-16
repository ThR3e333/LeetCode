# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:

        def backtracking(node):
            # Append the current node's value to the path
            path.append(str(node.val))

            # If the current node is a leaf node, add the path to the result
            if not node.left and not node.right:
                return result.append('->'.join(path))

            # Recursively traverse the left subtree
            if node.left:
                backtracking(node.left)
                path.pop()

            # Recursively traverse the right subtree
            if node.right:
                backtracking(node.right)
                path.pop()

        if not root:
            return []

        path, result = [], []
        backtracking(root)

        return result