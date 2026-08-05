class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # topological sort
        adj = {i: [] for i in range(numCourses)}
        indegree = [0] * numCourses

        for a,b in prerequisites:
            adj[b].append(a) # finished b can unlock a
            indegree[a] += 1 # how many courses need to be unlock if i learn a
        
        visited = []
        q = deque()
        for idx, n in enumerate(indegree):
            if n == 0:
                q.append(idx)
        
        while q:
            cur = q.popleft()
            visited.append(cur)
            for i in adj[cur]:
                if i not in visited:
                    indegree[i] -= 1
                if indegree[i] == 0:
                    q.append(i)
        return True if len(visited) == numCourses else False
