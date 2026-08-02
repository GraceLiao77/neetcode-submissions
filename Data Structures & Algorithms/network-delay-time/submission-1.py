class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # dijkstra
        adj = defaultdict(list)
        for u,v,t in times:
            adj[u].append((v,t))
        
        minHeap = [(0,k)] # time, node
        visited = set()
        totaltime = 0
        
        while minHeap:
            time, node = heapq.heappop(minHeap)
            if node in visited:
                continue
            visited.add(node)
            totaltime = max(totaltime, time)
            for v,t in adj[node]:
                if v not in visited:
                    heapq.heappush(minHeap, (t+time, v))
        return totaltime if len(visited) == n else -1
        
        # dfs
        # adj = defaultdict(list)
        # for u, v, w in times:
        #     adj[u].append((v, w))

        # dist = {node: float('inf') for node in range(1, n+1)}

        # def dfs(curnode, t):
        #     if t >= dist[curnode]:
        #         return
        #     dist[curnode] = t
        #     for v, w in adj[curnode]:
        #         dfs(v, w+t)
           
        # dfs(k, 0)
        # print(dist)
        # res = max(dist.values())
        # return res if res < float('inf') else -1