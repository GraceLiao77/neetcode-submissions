class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # base each row, every time check if next row item in the same col or diagonal
        col = set()
        posDiag = set() #\
        negDiag = set() #/

        res = []
        board = [['.'] * n for _ in range(n)]

        def dfs(r):
            if r == n:
                cp = [''.join(b) for b in board]
                res.append(cp)
                return
            for c in range(n):
                if board[r][c] != '.' or c in col or r-c in posDiag or r+c in negDiag:
                    continue
                # choice 
                board[r][c] = 'Q'
                col.add(c)
                posDiag.add(r-c)
                negDiag.add(r+c)

                dfs(r+1)

                # undo
                board[r][c] = '.'
                col.remove(c)
                posDiag.remove(r-c)
                negDiag.remove(r+c)
            

        dfs(0)
        return res
