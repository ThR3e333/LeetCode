# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        '''
        Find all root-to-leaf paths in the binary tree that sum up to the given target sum.

        :param root: The root node of the binary tree.
        :param targetSum: The target sum.
        :return: A list of paths that sum up to the target sum.
        '''
        def backtracking(node, targetSum):
            # Add the current node's value to the path
            path.append(node.val)

            # Check if it is a leaf node and the path sum equals the target sum
            if not node.left and not node.right and sum(path) == targetSum:
                result.append(path[:])

            # Recurse on the left child
            if node.left:
                backtracking(node.left, targetSum)

                # Remove the left child from the path
                path.pop()

            # Recurse on the right child
            if node.right:
                backtracking(node.right, targetSum)

                # Remove the right child from the path
                path.pop()

        if not root:
            return []

        path, result = [], []
        backtracking(root, targetSum)

        return result