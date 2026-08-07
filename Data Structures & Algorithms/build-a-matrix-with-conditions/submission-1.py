class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        # 2 0 0
        # 0 0 1
        # 0 3 0
        def topological(l):
            adj = {i: [] for i in range(k+1)}
            indegree = [0] * (k+1)
            for a,b in l:
                adj[a].append(b)
                indegree[b] += 1
            q = deque([i for i,item in enumerate(indegree) if item == 0])
            visited = []
            while q:
                cur = q.popleft()
                if cur not in visited:
                    visited.append(cur)
                for i in adj[cur]:
                    indegree[i] -= 1
                    if indegree[i] == 0:
                        q.append(i)
            visited.pop(0)
            return visited if len(visited) == k else []
        
        row = topological(rowConditions)
        col = topological(colConditions)
        if row == [] or col == []:
            return []
        # row[2,1,3] col[2,3,1]
        res = [[0] * k for _ in range(k)]
        for i,item in enumerate(row):
            j = col.index(item)
            res[i][j] = item
        return res
