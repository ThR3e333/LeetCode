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
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def getDepth(root, temp):
            global depth
            if not root.left and not root.right:
                depth = min(depth, temp)
                return
            if root.left:
                getDepth(root.left, temp+1)
            if root.right:
                getDepth(root.right, temp+1)
        if not root:
            return 0
        global depth
        depth = float('inf')
        getDepth(root, 0)
        return depth+1

# Approach 2

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        depth = float('inf')
        if root.left:
            depth = min(self.minDepth(root.left), depth)
        if root.right:
            depth = min(self.minDepth(root.right), depth)
        return depth+1

# Approach 3

from collections import deque
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        que = deque([root])
        count = 0
        while que:
            size = len(que)
            count += 1
            for _ in range(size):
                node = que.popleft()
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
                if not node.left and not node.right:
                    return count