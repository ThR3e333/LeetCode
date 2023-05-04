# Approach 1

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        count = 0
        result = float('-inf')
        for i in range(len(nums)):
            count += nums[i]
            if count > result:
                result = count
            if count < 0:
                count = 0
        return result

# Approach 2

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        dp = [0]*len(nums)
        dp[0] = nums[0]
        result = dp[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1]+nums[i], nums[i])
            result = max(result, dp[i])
        return result