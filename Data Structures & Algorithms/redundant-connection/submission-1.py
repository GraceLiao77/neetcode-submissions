class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        #   Disjoint set union
        n = len(edges)+1
        parent = [-1] * n

        def find(x):
            while parent[x] > 0:
                x = parent[x]
            return x

        for a, b in edges:
            rootA, rootB = find(a), find(b)
            if rootA == rootB:
                return [a, b]
            parent[rootA] = rootB
        return []