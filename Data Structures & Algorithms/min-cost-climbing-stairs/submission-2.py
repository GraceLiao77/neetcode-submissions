class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # optimized
        for i in range(len(cost)-3, -1, -1):
            cost[i] += min(cost[i+1], cost[i+2])
        return min(cost[0], cost[1])
        # cache = {}
        # def dfs(i):
        #     if i >= len(cost):
        #         return 0
        #     if i not in cache:
        #         cache[i] = cost[i] + min(dfs(i+1), dfs(i+2))
            
        #     return cache[i]

        # return min(dfs(0), dfs(1))