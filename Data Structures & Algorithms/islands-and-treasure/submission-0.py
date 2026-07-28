class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        row = len(grid)
        col = len(grid[0])
        def dfs(r, c, step):
            # out of range the grid, or next treasure chest
            if (r < 0 or c < 0 or r >= row or c >= col or 
                grid[r][c] == -1):
                return
            # already have a small value. so this is belong other chest
            if grid[r][c] < step:
                return
            grid[r][c] = step
            
            dfs(r-1, c, step+1)
            dfs(r+1, c, step+1)
            dfs(r, c+1, step+1)
            dfs(r, c-1, step+1)
        
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 0:
                    dfs(r, c, 0)
        

            

        