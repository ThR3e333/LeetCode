# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        '''
        Constructs a maximum binary tree from a list of integers.

        :param nums: The list of integers.
        :return: The root node of the constructed maximum binary tree.
        '''
        if not nums:
            return

        # Find the maximum value and its index in the list
        node_val = max(nums)
        node_index = nums.index(node_val)

        # Create a new node with the maximum value
        node = TreeNode(node_val)

        # Divide the list into left and right parts based on the maximum value's index
        left = nums[:node_index]
        right = nums[node_index + 1:]

        # Recursively construct the left and right subtrees
        node.left = self.constructMaximumBinaryTree(left)
        node.right = self.constructMaximumBinaryTree(right)

        return node