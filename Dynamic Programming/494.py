# Approach 1

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        totalSum = sum(nums)
        if abs(target) > totalSum:
            return 0
        dp = [[0]*(2*totalSum+1) for _ in range(len(nums))]
        if nums[0] == 0:
            dp[0][totalSum] = 2
        else:
            dp[0][totalSum-nums[0]] = 1
            dp[0][totalSum+nums[0]] = 1
        for i in range(1, len(nums)):
            for j in range(len(dp[0])):
                if j-nums[i]>0:
                    l = j - nums[i]
                else:
                    l = 0
                if j + nums[i] < len(dp[0]):
                    r = j + nums[i]
                else:
                    r = 0
                dp[i][j] = dp[i-1][l] + dp[i-1][r]
        return dp[len(nums)-1][totalSum+target]

# Approach 2

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        totalSum = sum(nums)
        if abs(target) > totalSum or (totalSum-target) % 2 == 1:
            return 0
        neg = (totalSum-target)//2
        dp = [[0]*(neg + 1) for _ in range(len(nums)+1)]
        dp[0][0] = 1
        for i in range(1,len(nums)+1):
            for j in range(neg+1):
                dp[i][j] = dp[i-1][j]
                if j >= nums[i-1]:
                    dp[i][j] += dp[i-1][j-nums[i-1]]
        return dp[len(nums)][neg]

# Approach 3

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        totalSum = sum(nums)
        if abs(target) > totalSum or (totalSum - target) % 2 == 1:
            return 0
        neg = (totalSum - target) // 2
        dp = [0] * (neg + 1)
        dp[0] = 1
        for i in range(len(nums)):
            for j in range(neg, nums[i] - 1, -1):
                dp[j] += dp[j - nums[i]]
        return dp[neg]