class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i: [] for i in range(n)}
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        visited = []
        total = 0
        def dfs(node, pre=-1):
            # leave node
            if adj[node] == []:
                return
            if node in visited:
                return
            
            visited.append(node)
            for item in adj[node]:
                if item != pre:
                    dfs(item, node)
            return

        for i in range(n):
            if i not in visited:
                total += 1
                dfs(i)
        
        return total
