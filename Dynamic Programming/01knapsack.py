# Approach 1

class Solution:
    def knapsack(self , V: int, n: int, vw: List[List[int]]) -> int:
        dp = [[0] * (V+1) for _ in range(n)]
        for j in range(V+1):
            if j >= vw[0][0]:
                dp[0][j] = vw[0][1]
        for i in range(1, n):
            for j in range(1, V+1):
                if j < vw[i][0]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-vw[i][0]]+vw[i][1])
        return dp[n-1][V]

# Approach 2

class Solution:
    def knapsack(self , V: int, n: int, vw: List[List[int]]) -> int:
        dp = [0] * (V+1)
        for i in range(n):
            for j in range(V, vw[i][0]-1, -1):
                dp[j] = max(dp[j], dp[j-vw[i][0]]+vw[i][1])
        return dp[V]