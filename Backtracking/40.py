# Approach 1

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        path, result = [], []
        candidates.sort()

        def backtracking(candidates, target, startIndex):
            if sum(path) > target:
                return
            if sum(path) == target:
                return result.append(path[:])
            for i in range(startIndex, len(candidates)):
                if sum(path) + candidates[i] > target:
                    return
                if i > startIndex and candidates[i] == candidates[i-1]:
                    continue
                path.append(candidates[i])
                backtracking(candidates, target, i+1)
                path.pop()
        backtracking(candidates, target, 0)
        return result

# Approach 2

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        global path, result, usage_list
        path, result = [], []
        usage_list = [False]*len(candidates)
        def backtracking(candidates, target, startIndex):
            if sum(path) == target:
                return result.append(path[:])
            for i in range(startIndex, len(candidates)):
                if sum(path) + candidates[i] > target:
                    return
                if i>0 and candidates[i] == candidates[i-1] and usage_list[i-1] == False:
                    continue
                path.append(candidates[i])
                usage_list[i] = True
                backtracking(candidates, target, i+1)
                usage_list[i] = False
                path.pop()
        candidates.sort()
        backtracking(candidates, target, 0)
        return result