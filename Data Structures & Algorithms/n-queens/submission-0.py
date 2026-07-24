class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()          # 存"这一列被占了"
        posDiag = set()       # 存"r + c 值被占了"（反对角线）
        negDiag = set()       # 存"r - c 值被占了"（主对角线）

        res = []
        box = [['.'] * n for _ in range(n)]

        def dfs(r):
            # finished every row box
            if r == n:
                res.append([''.join(r) for r in box])
                return
            # every row try every col
            for c in range(n):
                # whether can be choosed
                if c in cols or r+c in posDiag or r-c in negDiag:
                    continue

                # choice
                box[r][c] = 'Q'
                cols.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)

                # next line
                dfs(r+1)

                # undo
                box[r][c] = '.'
                cols.remove(c)
                posDiag.remove(r+c)
                negDiag.remove(r-c)
        dfs(0)
        return res