class Solution:
    def climbStairs(self, n: int) -> int:
        # DP bottom-up
        dp = [0] * (n+1)
        if n <= 2:
            return n
        dp[1], dp[2] = 1, 2
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]

        # cache = [-1] * n
        # def dfs(i):
        #     if i >= n:
        #         return i == n #true = 1 false=0
        #     if cache[i] != -1:
        #         return cache[i]
        #     cache[i] = dfs(i+1) + dfs(i+2)
        #     return cache[i]
        # return dfs(0)