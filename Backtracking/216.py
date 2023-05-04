# Approach 1

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        path, result = [], []

        def backtracking(k, n, startIndex):
            if sum(path) > n:
                return
            if sum(path) == n and len(path) == k:
                return result.append(path[:])
            for i in range(startIndex, 10):
                path.append(i)
                backtracking(k, n, i+1)
                path.pop()
        backtracking(k, n, 1)
        return result

# Approach 2

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        path, result = [], []

        def backtracking(k, n, startIndex):
            if sum(path) > n:
                return
            if sum(path) == n and len(path) == k:
                return result.append(path[:])
            for i in range(startIndex, 10-(k-len(path))+1):
                path.append(i)
                backtracking(k, n, i+1)
                path.pop()
        backtracking(k, n, 1)
        return result