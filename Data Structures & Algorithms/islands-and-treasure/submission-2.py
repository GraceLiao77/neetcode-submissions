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
                    q.append((r,c, 0))
        def add(r, c, s):
            if 0 <= r < row and 0 <= c < col and grid[r][c] == INF:
                grid[r][c] = s
                q.append((r, c, s))
        # bfs
        while q:
            r, c, s = q.popleft()
            add(r-1, c, s+1)
            add(r+1, c, s+1)
            add(r, c-1, s+1)
            add(r, c+1, s+1)

        

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
        