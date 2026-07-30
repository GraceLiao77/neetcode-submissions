class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # how many precourses are needed in every different course?
        preMap = {i: [] for i in range(numCourses)}
        # count number
        indegree = [0] * numCourses
        for a,b in prerequisites:
            preMap[b].append(a) # finished b can unlock a
            indegree[a] += 1
        
        q = deque() # current indefree is 0, which can be finised directly
        for i, item in enumerate(indegree):
            if item == 0:
                q.append(i)
        finalOrder = []
        print(q, indegree, preMap)
        while q:
            cur = q.popleft()
            finalOrder.append(cur)
            for x in preMap[cur]:
                indegree[x] -= 1
                if indegree[x] == 0:
                    q.append(x)
        print(finalOrder)
        if len(finalOrder) == numCourses:
            return finalOrder
        return []