class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # create adjacency list
        adj = {i: [] for i in range(numCourses)}
        for a,b in prerequisites:
            adj[b].append(a) # after finished b, u can take a
        # check if the list have circle
        # 0 - uncheck 1 - checking 2 - checked
        coursesState = [0] * numCourses
        def dfs(n):
            if coursesState[n] == 1:
                return False
            if coursesState[n] == 2:
                return True
            coursesState[n] = 1 # 0->1
            for j in adj[n]:
                if not dfs(j):
                    return False
            coursesState[n] = 2 # 1->2
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True