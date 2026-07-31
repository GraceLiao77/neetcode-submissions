class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        adj = {i: [] for i in range(n)}
        # store double direction
        for x,y in edges:
            adj[x].append(y)
            adj[y].append(x)
        
        visited = set()
        # 0,-1 -> visitied[0] dfs(1,0) | 1,0 -> v[0,1] dfs(2,1)dfs(3,1)dfs(4,1) |
        # 2,1 v[0,1,2]dfs(3,2)
        # 3,1
        # 4,1
        # 3,2 v[0,1,2,3] dfs(1,3) false
        def dfs(c, p):
            if c in visited:
                return False
            visited.add(c)
            for i in adj[c]:
                if i == p:
                    continue
                if not dfs(i, c):
                    return False
            return True
        # not only check circle but also check the number of node
        return dfs(0, -1) and len(visited) == n