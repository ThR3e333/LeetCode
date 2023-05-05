class Solution:
    def removeDuplicates(self, s: str) -> str:
        '''
        Given a string consisting of lowercase letters, removes adjacent duplicates and return the modified string.

        :param s: A string consisting of lowercase letters.
        :return: A string with adjacent duplicates removed.
        '''
        stack = []
        for i in s:
            # If the current character is equal to the top of the stack, pop it
            if stack and i == stack[-1]:
                stack.pop()

            # Otherwise, append the current character to the stack
            else:
                stack.append(i)

        return ''.join(stack)