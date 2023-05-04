class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        dp = [[0]*(2*k+1) for _ in range(len(prices))]
        for j in range(1, 2*k+1):
            if j%2 == 1:
                dp[0][j] = -prices[0]
        for i in range(1, len(prices)):
            for j in range(1, 2*k+1):
                if j%2 == 1:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]-prices[i])
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]+prices[i])
        return dp[-1][-1]