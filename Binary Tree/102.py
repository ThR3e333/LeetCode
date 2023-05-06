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
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        '''
        Given a binary tree, returns the level order traversal of its nodes' values.

        :param root: The root of the binary tree.
        :return: The level order traversal of the binary tree.
        '''
        if not root:
            return []

        # Initialize a queue for breadth-first search and a result list
        que, result = deque(), []
        que.append(root)

        # Perform breadth-first search
        while que:
            # Initialize a temporary list to store nodes at the current level
            temp = []
            level_size = len(que)

            # Process all nodes at the current level
            for _ in range(level_size):
                node = que.popleft()
                temp.append(node.val)

                # Add the node's children to the queue, if they exist
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)

            result.append(temp)

        return result

# Approach 2

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        '''
        Given a binary tree, returns the level order traversal of its nodes' values.

        :param root: The root of the binary tree.
        :return: The level order traversal of the binary tree.
        '''
        if not root:
            return []

        def traverse(node, level):
            '''
            Helper function to traverse the binary tree in level order.

            :param node: The root node of the binary tree.
            :param level: The level of the current node in the binary tree.
            :return:
            '''
            if not node:
                return

            # If the current level is not in the result list, append a new empty list for it
            if len(result) == level:
                result.append([])

            # Add the current node's value to the appropriate level list
            result[level].append(node.val)

            # Recursively traverse the left and right subtrees with incremented level
            if node.left:
                traverse(node.left, level+1)
            if node.right:
                traverse(node.right, level+1)

        result = []
        traverse(root, 0)

        return result