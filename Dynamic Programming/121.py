# Approach 1

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0]*2 for _ in range(len(prices))]
        dp[0][0], dp[0][1] = -prices[0], 0
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][0], -prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][1]+prices[i])
        return dp[-1][1]

# Approach 2

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = float('inf')
        result = 0
        for i in range(len(prices)):
            low = min(low, prices[i])
            result = max(result, prices[i]-low)
        return result