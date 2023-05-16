# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        '''
        Finds the value of the leftmost node in the bottom row of a binary tree.

        :param root: The root node of the binary tree.
        :return: The value of the leftmost node in the bottom row.
        '''
        def traverse(node, current_depth):
            nonlocal max_depth, bottom_left_val

            # If it is a leaf node and the current depth is greater than the max depth so far,
            # update the max depth and assign the value of the leftmost node in the bottom row
            if not node.left and not node.right:
                if current_depth > max_depth:
                    max_depth = current_depth
                    bottom_left_val = node.val
                    return

            # Recursively traverse the left and right subtrees, incrementing the current depth
            if node.left:
                traverse(node.left, current_depth + 1)
            if node.right:
                traverse(node.right, current_depth + 1)

        max_depth = float('-inf')
        bottom_left_val = 0

        traverse(root, 0)

        return bottom_left_val


from collections import deque
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        '''
        Finds the value of the leftmost node in the bottom row of a binary tree.

        :param root: The root node of the binary tree.
        :return: The value of the leftmost node in the bottom row.
        '''
        que = deque([root])
        result = []

        while que:
            level_size = len(que)

            # Append the value of the leftmost node in the current level
            result.append(que[0].val)

            # Process all nodes at the same level
            for _ in range(level_size):
                node = que.popleft()

                # Enqueue the left and right child nodes, if they exist
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)

        return result[-1]

