class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        global path, result
        path, result = [], []
        def backtracking(nums, startIndex):
            if len(path)>1:
                result.append(path[:])
            if startIndex == len(nums):
                return
            usage_list = set()
            for i in range(startIndex, len(nums)):
                if (path and nums[i] < path[-1]) or nums[i] in usage_list:
                    continue
                path.append(nums[i])
                usage_list.add(nums[i])
                backtracking(nums, i+1)
                path.pop()
        backtracking(nums, 0)
        return result