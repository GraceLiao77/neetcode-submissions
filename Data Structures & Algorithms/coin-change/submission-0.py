class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}
        def dfs(i):
            if i == 0:
                return 0
            if i < 0:
                return -1
            if i in cache:
                return cache[i]
            best = float('inf')
            for coin in coins:
                if coin <= i:
                    sub = dfs(i - coin)
                    if sub != -1:
                        best = min(best, sub+1)
            cache[i] = best if best != float('inf') else -1
            return cache[i]
        return dfs(amount)