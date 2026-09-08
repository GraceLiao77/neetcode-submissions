class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # 前i个coin up to j
        # dp[i][j] = dp[i][j-coin] + dp[i-1][j]

        dp = [[0] * (amount+1) for _ in range(len(coins)+1)]
        for i in range(len(coins)+1):
            dp[i][0] = 1
        
        for i in range(1, len(coins)+1):
            for j in range(1, amount+1):
                # no use cur
                dp[i][j] = dp[i-1][j]
                # use cur
                if j >= coins[i-1]:
                    dp[i][j] += dp[i][j-coins[i-1]]
        return dp[-1][-1]