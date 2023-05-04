class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        path, result = [], []
        candidates.sort()

        def backtracking(candidates, target):
            if sum(path) > target:
                return
            if sum(path) == target:
                return result.append(path[:])

            for i in range(len(candidates)):
                if sum(path) + candidates[i] > target:
                    return
                path.append(candidates[i])
                backtracking(candidates[i:], target)
                path.pop()

        backtracking(candidates, target)

        return result