class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}
        def dfs(i):
            if i == 0:
                return 0
            if i < 0:
                return float('inf')
            if i in cache:
                return cache[i]
            best = float('inf')
            for coin in coins:
                if i - coin >= 0:
                    best = min(best, 1+dfs(i-coin))
            cache[i] = best
            return cache[i]
        return dfs(amount) if dfs(amount) != float('inf') else -1