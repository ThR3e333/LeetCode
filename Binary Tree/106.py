# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        '''
        Build a binary tree from inorder and postorder traversals.

        :param inorder: The inorder traversal of the tree.
        :param postorder: The postorder traversal of the tree.
        :return: The root node of the constructed tree.
        '''
        if not postorder:
            return
        # The last element in the postorder traversal is the root of tree to be constructed
        root_val = postorder[-1]
        root = TreeNode(root_val)

        # Find the index of the root node in the inorder traversal
        node_index = inorder.index(root_val)

        # Split the inorder and postorder traversals into left and right subtrees
        left_inorder = inorder[:node_index]
        right_inorder = inorder[node_index + 1:]

        left_postorder = postorder[:len(left_inorder)]
        right_postorder = postorder[len(left_inorder):len(postorder) - 1]

        # Recursively build the left and right subtrees
        root.left = self.buildTree(left_inorder, left_postorder)
        root.right = self.buildTree(right_inorder, right_postorder)

        return root