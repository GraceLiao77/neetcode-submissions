class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time = 0
        row, col = len(grid), len(grid[0])
        freshCount = 0

        q = deque()

        for r in range(row):
            for c in range(col):
                # start from every rotten fruit
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    freshCount += 1

        def changeFreshToRotten(r, c):
            nonlocal freshCount
            if 0 <= r < row and 0 <= c < col and grid[r][c] == 1:
                grid[r][c] = 2
                freshCount -= 1
                q.append((r, c))

        while q and freshCount > 0:
            for item in range(len(q)):
                r, c = q.popleft()
                changeFreshToRotten(r-1, c)
                changeFreshToRotten(r+1, c)
                changeFreshToRotten(r, c-1)
                changeFreshToRotten(r, c+1)
            time += 1

        # still have 
        if freshCount != 0:
            return -1
        return time