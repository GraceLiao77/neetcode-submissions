class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        row, col = len(matrix), len(matrix[0])
        direction = [[1,0],[-1,0],[0,1],[0,-1]]
        memo = {} # return the max length from r,c 

        def dfs(r, c):
            if (r, c) in memo:
                return memo[(r,c)]
            maxLen = 1
            for a,b in direction:
                nr, nc = r+a, c+b
                if 0 <= nr < row and 0 <= nc < col and matrix[nr][nc] > matrix[r][c]:
                    maxLen = max(maxLen, 1 + dfs(nr, nc))
            memo[(r,c)] = maxLen
            return maxLen
        res = 0
        for r in range(row):
            for c in range(col):
                res = max(res, dfs(r, c))
        
        return res

