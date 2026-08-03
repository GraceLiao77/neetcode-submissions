class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        visited = set()
        minHeap = [(grid[0][0], 0, 0)]
        direction = [(-1,0),(1,0),(0,-1),(0,1)]

        visited = set()
        while minHeap:
            t, r, c = heapq.heappop(minHeap)
            if (r, c) in visited:        # ← 加这个：已处理过就跳过
                continue
            if r == row-1 and c == col-1:
                return t
            visited.add((r,c))
            for i,j in direction:
                if (r+i,c+j) not in visited:
                    if 0 <= r+i < row and 0 <= c+j < col:
                        heapq.heappush(minHeap,(max(t,grid[r+i][c+j]), r+i, c+j))

