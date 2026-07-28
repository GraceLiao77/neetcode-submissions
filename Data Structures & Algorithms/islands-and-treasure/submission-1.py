class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # bfs
        row, col = len(grid), len(grid[0])
        q = deque()
        INF = 2147483647
        # all chest put in queue
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 0:
                    q.append((r,c,0))
        # bfs
        while q:
            r, c, step = q.popleft()
            step += 1
            for dr, dc in [(1,0), (-1,0), (0,1), (0, -1)]:
                newr, newc = r+dr, c+dc
                if (0 <= newr < row and 
                    0 <= newc < col and
                    grid[newr][newc] == INF):
                    grid[newr][newc] = step
                    q.append((newr, newc, step))

        # row = len(grid)
        # col = len(grid[0])
        # def dfs(r, c, step):
        #     # out of range the grid, or next treasure chest
        #     if (r < 0 or c < 0 or r >= row or c >= col or 
        #         grid[r][c] == -1):
        #         return
        #     # already have a small value. so this is belong other chest
        #     if grid[r][c] < step:
        #         return
        #     grid[r][c] = step
            
        #     dfs(r-1, c, step+1)
        #     dfs(r+1, c, step+1)
        #     dfs(r, c+1, step+1)
        #     dfs(r, c-1, step+1)
        
        # for r in range(row):
        #     for c in range(col):
        #         if grid[r][c] == 0:
        #             dfs(r, c, 0)
        