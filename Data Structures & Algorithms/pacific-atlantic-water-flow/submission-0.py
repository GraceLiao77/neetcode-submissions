class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row = len(heights) #3
        col = len(heights[0]) #5
        
        res = []
        def dfs(r, c, v, h):
            if r < 0 or c < 0 or r >= row or c >= col:
                return False, False
            if heights[r][c] > h:
                return False, False
            if (r, c) in v:
                return False, False
            v.add((r, c))
            pac = (r==0 or c==0)
            atl = (r==row-1 or c == col-1)

            for x,y in [(1,0),(-1,0),(0,1),(0,-1)]:
                p, a = dfs(r+x, c+y, v, heights[r][c])
                pac = pac or p
                atl = atl or a
            
            return pac, atl

        for r in range(row):
            for c in range(col):
                visited = set()
                pac, atl = dfs(r, c, visited, heights[r][c])
                if pac and atl:
                    res.append([r, c])
        return res
