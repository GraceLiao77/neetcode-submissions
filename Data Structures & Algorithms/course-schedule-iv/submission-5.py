class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = {i: [] for i in range(numCourses)}
        indegree = [0] * numCourses

        for a,b in prerequisites:
            adj[a].append(b)
            indegree[b] += 1
        print(adj)
        prelist = {i: set() for i in range(numCourses)} #all pre list
        q = deque()
        for i, item in enumerate(indegree):
            if item == 0:
                q.append(i)
        while q:
            cur = q.popleft()
            for i in adj[cur]:
                prelist[i].add(cur) # 加入直接前置
                prelist[i] |= prelist[cur] # ｜=并集，把cur的前置也加入进去
                indegree[i] -= 1
                if indegree[i] == 0:
                    q.append(i)
        res = []
        for i,j in queries:
            if i in prelist[j]:
                res.append(True)
            else:
                res.append(False)
        return res