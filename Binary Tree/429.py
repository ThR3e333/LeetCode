"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

from collections import deque
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        result = []
        que = deque([root])
        while que:
            temp = []
            size = len(que)
            for _ in range(size):
                node = que.popleft()
                temp.append(node.val)
                if node.children:
                    que.extend(node.children)
            result.append(temp)
        return result