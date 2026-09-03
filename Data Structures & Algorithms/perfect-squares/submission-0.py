class Solution:
    def numSquares(self, n: int) -> int:
        square = []
        for i in range(1, n+1):
            cur = pow(i,2)
            if cur <= n:
                square.append(cur)
        dp = [float('inf')] * (n+1) # 凑出数字 i 所需的最少完全平方数个数
        dp[0] = 0

        for s in square: #[1,4,9,16,25,...]
            for i in range(s, n+1):
                dp[i] = min(dp[i], dp[i-s]+1)
        return -1 if dp[n] == float('inf') else dp[n]

