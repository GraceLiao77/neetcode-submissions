class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # dp[i][j] = dp[i-1][j] + dp[i][j-1]
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1
        for i in range(0, m):
            for j in range(0, n):
                if i-1 < 0 and j-1 < 0:
                    continue
                if i-1 < 0 and j-1 > 1:
                    dp[i][j] = dp[i][j-1]
                elif i-1 > 1 and j-1 < 0:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]
