class Solution:
    def isValid(self, s: str) -> bool:
        '''
        Determines whether a given string of parentheses is valid.

        :param s: A string containing only parentheses.
        :return: True if the string contains a valid combination of parentheses, False otherwise.
        '''
        # Create a hash map to store the match brackets
        hash_map = {'(': ')', '[': ']', '{': '}'}

        # Create an empty stack to store the opening brackets
        stack = []
        for i in s:
            # If the character is an opening bracket, push its matching closing bracket into the stack
            if i in hash_map.keys():
                stack.append(hash_map[i])

            # If the character is an closing bracket, check if it matches the top element of the stack
            elif stack and i == stack[-1]:
                stack.pop()
            else:
                return False

        # If the stack is empty after iterating through the input string, return True
        # False otherwise
        return True if not stack else False
