class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Prim's
        # prims 每次从已经找到的最小edge点出发 and kruskal 每次全图找最小的edge，如果成环则continue
        n = len(points)
        visited = [False] * n
        minDist = [float('inf')] * n
        # start from 0
        minDist[0] = 0
        res = 0

        for _ in range(n):
            v = -1 # 还没有最小点，目前找到的最小点
            for i in range(n):
                # find not visited and the minDist, v=-1第一个不需要校验大小直接进，后面才会和最小dist比较
                if not visited[i] and (v == -1 or minDist[i] < minDist[v]):
                    v = i
            # 找到目前最小点
            visited[v] = True
            res += minDist[v]
            x,y = points[v]
            # 统计没访问过的节点距离当前节点的距离
            for i in range(n):
                if not visited[i]:
                    nx,ny = points[i]
                    minDist[i] = min(minDist[i], abs(x-nx)+abs(y-ny))
        return res



        # l = len(points)
        # adj = {i: [] for i in range(l)}
        # for i in range(l):
        #     x1,y1 = points[i]
        #     for j in range(i+1,l):
        #         x2,y2 = points[j]
        #         distance = abs(x1-x2)+abs(y1-y2)
        #         adj[i].append((distance, j))
        #         adj[j].append((distance, i))
        # # print(adj)
        # visited = set()
        # res = 0
        # heap = [[0,0]]
        # while heap:
        #     dist, i = heapq.heappop(heap)
        #     if i in visited:
        #         continue
        #     visited.add(i)
        #     res += dist
        #     for neiDist, nei in adj[i]:
        #         if nei not in visited:
        #             heapq.heappush(heap, [neiDist, nei])
        # return res