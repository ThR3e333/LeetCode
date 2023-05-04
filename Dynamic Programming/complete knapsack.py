# Approach 1

# class Solution:
#     def knapsack(self, V, n, vw) -> int:
#         dp = [[0] * (V+1) for _ in range(n)]
#         for i in range(n):
#             for j in range(1,V+1):
#                 dp[i][j] = max(dp[i-1][j], dp[i][j-vw[i][0]]+vw[i][1])
#         print(dp)
#         return dp[n-1][V]

# Approach 2

# class Solution:
#     def knapsack(self, V, n, vw) -> int:
#         dp = [0] * (V+1)
#         for i in range(n):
#             for j in range(vw[i][0], V+1):
#                 dp[j] = max(dp[j], dp[j-vw[i][0]]+vw[i][1])
#         return dp[V]

# Approach 3

class Solution:
    def knapsack(self, V, n, vw) -> int:
        dp = [0] * (V+1)
        for j in range(1, V+1):
            for i in range(n):
                if j >= vw[i][0]:
                    dp[j] = max(dp[j], dp[j-vw[i][0]]+vw[i][1])
        return dp[V]

V = 4
n = 3
vw = [[1, 15], [3, 20], [4, 30]]
solution = Solution
print(solution.knapsack(self=Solution, V=V, n=n, vw=vw))