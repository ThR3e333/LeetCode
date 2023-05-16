# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Approach 1

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        '''
        Counts the total number of the nodes in a binary tree.

        :param root: The root node of the binary tree.
        :return: The total number of nodes in the binary tree.
        '''
        def getNum(root):
            if not root:
                return 0

            # Recursively count the number of nodes in the left and right subtrees
            left = getNum(root.left)
            right = getNum(root.right)

            # Total number of nodes is the sum of nodes in the left subtree,
            # nodes in the right subtree, and the current node itself
            total = left + right + 1

            return total

        return getNum(root)

# Approach 2

from collections import deque
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        '''
        Counts the total number of the nodes in a binary tree.

        :param root: The root node of the binary tree.
        :return: The total number of nodes in the binary tree.
        '''
        if not root:
            return 0

        count = 0
        que = deque([root])

        while que:
            size = len(que)
            count += size

            for _ in range(size):
                node = que.popleft()

                # Add left child of the current node to the queue
                if node.left:
                    que.append(node.left)

                # Add right child of the current node to the queue
                if node.right:
                    que.append(node.right)

        return count