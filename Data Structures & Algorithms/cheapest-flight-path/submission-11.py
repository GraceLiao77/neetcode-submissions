class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = {i: [] for i in range(n)}
        for s,d,cost in flights:
            adj[s].append([d, cost])
        memo = {} # store the cost from node to dst 
            # nodecount剩余可走边数
        def dfs(node, nodecount):
            if node == dst:
                return 0
            if nodecount == 0:
                return -1
            if (node,nodecount) in memo:
                return memo[(node,nodecount)]
            res = float('inf')
            for c,cost in adj[node]:
                cur = dfs(c, nodecount-1)
                if cur != -1:
                    res = min(res, cur+cost)
            memo[(node, nodecount)] = res if res != float('inf') else -1
            return memo[(node, nodecount)]

        return dfs(src, k+1)
