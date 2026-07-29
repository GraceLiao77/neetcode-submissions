class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # from edge to center
        row, col = len(board), len(board[0])
        visited = set()

        def dfs(r, c, visited):
            if r < 0 or c < 0 or r >= row or c >= col:
                return
            if (r,c) in visited:
                return
            if board[r][c] == 'X':
                return
            visited.add((r,c))
            dfs(r-1,c,visited)
            dfs(r+1,c,visited)
            dfs(r,c-1,visited)
            dfs(r,c+1,visited)

        for r in range(row):
            for c in range(col):
                if ((r == 0 or c == 0 or
                    r == row-1 or c == col-1) and
                    board[r][c] == 'O'):
                    dfs(r, c, visited)
        print(visited)
        for r in range(row):
            for c in range(col):
                if (r, c) not in visited:
                    board[r][c] = 'X'
