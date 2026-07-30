class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # BFS
        preMap = {i: [] for i in range(numCourses)}
        indegree = [0] * numCourses # 每门课程的入度（前置课程个数）
        for a, b in prerequisites:
            preMap[b].append(a) # -> 修完b解锁的课程
            indegree[a] += 1
        
        # indegree == 0 进入代表没有前置课程
        q = deque()
        for i, val in enumerate(indegree):
            if val == 0:
                q.append(i)
        count = 0 # 目前修的课
        while q:
            count += 1
            cur_course = q.pop()
            for x in preMap[cur_course]:
                indegree[x] -= 1
                if indegree[x] == 0:
                    q.append(x)
        return True if count == numCourses else False
