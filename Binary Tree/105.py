# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        '''
        Build a binary tree from preorder and inorder traversals.

        :param preorder: The preorder traversal of the tree.
        :param inorder: The inorder traversal of the tree.
        :return: The root node of the constructed tree.
        '''
        if not preorder:
            return

        # The first element in the preorder traversal is the root of tree to be constructed
        root_val = preorder[0]
        root = TreeNode(root_val)

        # Find the index of the root node in the inorder traversal
        node_index = inorder.index(root_val)

        # Split the inorder and preorder traversals into left and right subtrees
        left_inorder = inorder[:node_index]
        right_inorder = inorder[node_index + 1:]

        left_preorder = preorder[1:1 + len(left_inorder)]
        right_preorder = preorder[1 + len(left_inorder):]

        # Recursively build the left and right subtrees
        root.left = self.buildTree(left_preorder, left_inorder)
        root.right = self.buildTree(right_preorder, right_inorder)

        return root