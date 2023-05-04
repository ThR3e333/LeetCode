class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[2] = 1
        for i in range(3, len(dp)):
            for j in range(1, i//2+1):
                dp[i] = max(dp[i], max(j*(i-j), j*dp[i-j]))
        return dp[n]