# Approach 1

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        global path, result
        path, result = [], []
        def backtracking(nums, startIndex):
            result.append(path[:])
            if startIndex == len(nums):
                return
            for i in range(startIndex, len(nums)):
                if i > startIndex and nums[i] == nums[i-1]:
                    continue
                path.append(nums[i])
                backtracking(nums, i+1)
                path.pop()
        nums.sort()
        backtracking(nums, 0)
        return result

# Approach 2

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        global path, result, usage_list
        path, result = [], []
        usage_list = [False] * len(nums)

        def backtracking(nums, startIndex):
            result.append(path[:])
            if startIndex == len(nums):
                return
            for i in range(startIndex, len(nums)):
                if i > 0 and nums[i] == nums[i - 1] and usage_list[i - 1] == False:
                    continue
                path.append(nums[i])
                usage_list[i] = True
                backtracking(nums, i + 1)
                usage_list[i] = False
                path.pop()

        nums.sort()
        backtracking(nums, 0)
        return result