class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        global path, result
        path, result = [], []
        def backtracking(nums, startIndex):
            result.append(path[:])
            if startIndex == len(nums):
                return
            for i in range(startIndex, len(nums)):
                path.append(nums[i])
                backtracking(nums, i+1)
                path.pop()
        backtracking(nums, 0)
        return result