# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        def traverse(node, current_depth):
            nonlocal max_depth, bottom_left_val
            if not node.left and not node.right:
                if current_depth > max_depth:
                    max_depth = current_depth
                    bottom_left_val = node.val
                    return
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
        que = deque([root])
        result = []
        while que:
            level_size = len(que)
            result.append(que[0].val)
            for _ in range(level_size):
                node = que.popleft()
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
        return result[-1]

