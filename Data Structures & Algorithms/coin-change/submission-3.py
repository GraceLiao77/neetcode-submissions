class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        dp = [float('inf')] * (amount+1) # dp[i]凑到金额i需要的最小硬币个数
        dp[0] = 0
        for i in range(1, amount+1):
            for c in coins:
                if i >= c:
                    # pick c # not pick
                    dp[i] = min(dp[i], dp[i-c] + 1)
        print(dp)
        return -1 if dp[amount] == float('inf') else dp[amount]
