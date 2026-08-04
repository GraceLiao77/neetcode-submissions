class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        l = len(points)
        adj = {i: [] for i in range(l)}
        for i in range(l):
            x1,y1 = points[i]
            for j in range(i+1,l):
                x2,y2 = points[j]
                distance = abs(x1-x2)+abs(y1-y2)
                adj[i].append((distance, j))
                adj[j].append((distance, i))
        # print(adj)
        visited = set()
        res = 0
        heap = [[0,0]]
        while heap:
            dist, i = heapq.heappop(heap)
            if i in visited:
                continue
            visited.add(i)
            res += dist
            for neiDist, nei in adj[i]:
                if nei not in visited:
                    heapq.heappush(heap, [neiDist, nei])
        return res



                