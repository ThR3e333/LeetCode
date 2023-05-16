'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
'''

# Approach 1

from collections import deque
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        '''
        Perform level order traversal, starting from the bottom.

        :param root: The root node of the binary tree.
        :return: The level order traversal, starting from the bottom.
        '''
        if not root:
            return []

        result = []
        # Create a deque and enqueue the root node
        que = deque([root])

        while que:
            # Temporary list to store the nodes at the current level
            temp = []

            # Get the number of nodes at the current level
            size = len(que)

            # Process nodes at the current level
            for _ in range(size):
                # Dequeue a node from the front of the queue
                node = que.popleft()

                # Append the node's value to the temporary list
                temp.append(node.val)

                # Enqueue the left and right child nodes if they exists
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)

            # Append the nodes at the current level to the result list
            result.append(temp)

        # Reverse the result list to get the level order traversal starting from the bottom
        return result[::-1]

# Approach 2

class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        '''
        Perform level order traversal, starting from the bottom.

        :param root: The root node of the binary tree.
        :return: The level order traversal, starting from the bottom.
        '''
        if not root:
            return []
        result = []

        def helper(root, level):
            # If the current level is not present in the result list, add an empty list for the level
            if len(result) == level:
                result.append([])

            # Append the current node's value to the corresponding level list
            result[level].append(root.val)

            # Process the left and right children recursively
            if root.left:
                helper(root.left, level+1)
            if root.right:
                helper(root.right, level+1)

        helper(root, 0)

        # Reverse the result list to get the level order traversal starting from the bottom
        return result[::-1]