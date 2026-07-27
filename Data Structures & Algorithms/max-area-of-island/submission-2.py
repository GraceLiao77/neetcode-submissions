class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        res = 0
        def dfs(r, c, l):
            # finished
            if r < 0 or c < 0 or r >= row or c >= col or grid[r][c] == 0:
                return 0
            # count
            grid[r][c] = 0
            return 1 + dfs(r+1, c, l) + dfs(r-1, c, l) + dfs(r, c+1, l) + dfs(r, c-1, l)


        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    res =max(dfs(r, c, 0), res) 

        return res