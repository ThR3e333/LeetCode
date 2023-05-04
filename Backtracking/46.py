# Approach 1

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        global path, result
        path, result = [], []

        def backtracking(nums):
            if len(path) == len(nums):
                return result.append(path[:])
            for i in nums:
                if i in path:
                    continue
                path.append(i)
                backtracking(nums)
                path.pop()
        backtracking(nums)
        return result

# Approach 2

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        global path, result, usage_list
        path, result = [], []
        usage_list = [False] * len(nums)
        def backtracking(nums):
            if len(path) == len(nums):
                return result.append(path[:])
            for i in range(len(nums)):
                if usage_list[i] == True:
                    continue
                usage_list[i] = True
                path.append(nums[i])
                backtracking(nums)
                path.pop()
                usage_list[i] = False
        backtracking(nums)
        return result