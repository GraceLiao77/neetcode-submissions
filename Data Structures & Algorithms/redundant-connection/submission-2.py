class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        #   Disjoint set union
        n = len(edges)+1
        parents = [i for i in range(n+1)]

        def findroot(x):
            while parents[x] != x:
                x = parents[x]
            return x
        # 1 2 3 4 parents
        # 1 3 4 4 parents[x]
        for x,y in edges:
            rx,ry = findroot(x), findroot(y)
            if rx == ry:
                return [x, y]
            parents[rx] = ry
            
        return []
