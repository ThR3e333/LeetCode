# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Approach 1

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def getNum(root):
            if not root:
                return 0
            left = getNum(root.left)
            right = getNum(root.right)
            total = left + right + 1
            return total
        return getNum(root)

# Approach 2

from collections import deque
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        count = 0
        que = deque([root])
        while que:
            size = len(que)
            count += size
            for _ in range(size):
                node = que.popleft()
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
        return count