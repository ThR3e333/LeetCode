class Solution:
    def partition(self, s: str) -> List[List[str]]:
        path, result = [], []
        def backtracking(s, startIndex):
            if startIndex >= len(s):
                return result.append(path[:])
            for i in range(startIndex, len(s)):
                temp = s[startIndex:i+1]
                if temp == temp[::-1]:
                    path.append(temp)
                    backtracking(s, i+1)
                    path.pop()
                else:
                    continue
        backtracking(s, 0)
        return result