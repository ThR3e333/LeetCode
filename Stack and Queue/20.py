class Solution:
    def isValid(self, s: str) -> bool:
        hash_map = {'(': ')', '[': ']', '{': '}'}
        stack = []
        for i in s:
            if i in hash_map.keys():
                stack.append(hash_map[i])
            elif stack and i == stack[-1]:
                stack.pop()
            else:
                return False
        return True if not stack else False
