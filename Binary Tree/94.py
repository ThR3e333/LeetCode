'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
'''

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        '''
        Returns the inorder traversal of a binary tree.

        :param root: The root node of the binary tree.
        :return: A list of integers representing the inorder traversal of the binary tree.
        '''
        result = []

        # Define a helper function to traverse the binary tree in order
        def inorder_traversal(node):
            # If the node is None, return
            if node == None:
                return

            # Recursively traverse the left subtree
            inorder_traversal(node.left)

            # Append the current node's value to the result list
            result.append(node.val)

            # Recursively traverse the right subtree
            inorder_traversal(node.right)

        inorder_traversal(root)

        return result

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        '''
        Returns the inorder traversal of a binary tree.

        :param root: The root node of the binary tree.
        :return: A list of integers representing the inorder traversal of the binary tree.
        '''
        if not root:
            return []

        stack, result = [], []

        # Traverse the tree using iterative inorder traversal
        current_node = root
        while stack or current_node:
            # If the current node is not None, push it onto the stack and move to its left child
            if current_node:
                stack.append(current_node)
                current_node = current_node.left

            # If the current node is None, pop the last node from the stack,
            # append its value to the result list, and move to its right child
            else:
                current_node = stack.pop()
                result.append(current_node.val)
                current_node = current_node.right

        return result