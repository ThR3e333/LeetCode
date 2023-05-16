'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
'''

# Approach 1

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        '''
        Perform a preorder traversal of a binary tree.

        :param root: The root node of the binary tree.
        :return: A list of integers representing the preorder traversal of the binary tree.
        '''
        result = []

        def traversal(node):
            # Base case: if the root is None, return
            if node == None:
                return

            # Append the current node's value to the result list
            result.append(node.val)

            # Recurse on the left subtree
            traversal(node.left)

            # Recurse on the right subtree
            traversal(node.right)

        traversal(root)

        return result

# Approach 2

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        stack, result = [root], []

        while stack:
            node = stack.pop()
            result.append(node.val)

            if node.right:
                stack.append(node.right)

            if node.left:
                stack.append(node.left)

        return result
