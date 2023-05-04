# Approach 1

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        path, result = [], []

        def backtracking(n, k, startIndex):
            if len(path) == k:
                return result.append(path[:])
            for i in range(startIndex, n+1):
                path.append(i)
                backtracking(n, k, i+1)
                path.pop()
        backtracking(n, k, 1)
        return result

# Approach 2

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        path, result = [], []

        def backtracking(n, k, startIndex):
            if len(path) == 2:
                return result.append(path[:])

            for i in range(startIndex, n-k+len(path)+2):
                path.append(i)
                backtracking(n, k, i+1)
                path.pop()
        backtracking(n, k, 1)
        return result