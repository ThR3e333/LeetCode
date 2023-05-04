class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hash_map = {'1': ' ', '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv',
                    '9': 'wxyz'}
        path, result = [], []
        if len(digits) == 0:
            return []

        def backtracking(digits, index):
            if index == len(digits):
                return result.append(''.join(path))
            for i in hash_map[digits[index]]:
                path.append(i)
                backtracking(digits, index + 1)
                path.pop()

        backtracking(digits, 0)
        return result