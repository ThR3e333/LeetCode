class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        global path, result, usage_list
        path, result = [], []
        usage_list = [False] * len(nums)
        def backtracking(nums):
            if len(path) == len(nums):
                return result.append(path[:])
            for i in range(len(nums)):
                if not usage_list[i]:
                    if i>0 and nums[i] == nums[i-1] and usage_list[i-1] == False:
                        continue
                    usage_list[i] = True
                    path.append(nums[i])
                    backtracking(nums)
                    path.pop()
                    usage_list[i] = False
        nums.sort()
        backtracking(nums)
        return result