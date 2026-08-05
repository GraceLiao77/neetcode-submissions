class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {i: [] for i in range(numCourses)}
        inDegree = [0] * numCourses
        for a,b in prerequisites:
            adj[b].append(a)
            inDegree[a] += 1
        visited = []
        q = deque()
        for i, item in enumerate(inDegree):
            if item == 0:
                q.append(i)
        while q:
            cur = q.popleft()
            visited.append(cur)
            for i in adj[cur]:
                inDegree[i] -= 1
                if inDegree[i] == 0:
                    q.append(i)
        return visited if len(visited) == numCourses else []