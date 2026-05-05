class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # bitmask
        row = [0] * 9
        col = [0] * 9
        square = [0] * 9

        # 1 << 0 = 000000001 number1, 1 << 1 = 000000010 number2, 1 << 4 = 000010000 number5
        # (1 << val) & rows[r], rows[r] = 00000101, 1 << 2 = 00000100, and = 00000100 != 0
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                val = int(board[r][c]) - 1
                if row[r] & (1 << val):
                    return False
                if col[c] & (1 << val):
                    return False
                if square[(r//3)*3+(c//3)] & (1 << val):
                    return False
                row[r] = row[r] | (1 << val)
                col[c] |= (1 << val)
                square[(r//3)*3+(c//3)] |= (1 << val)
        return True
                


        # hashset
        # row = defaultdict(set)
        # col = defaultdict(set)
        # square = defaultdict(set)

        # for r in range(9):
        #     for c in range(9):
        #         if board[r][c] == '.':
        #             continue
        #         if board[r][c] in row[r] or board[r][c] in col[c] or board[r][c] in square[(r // 3, c // 3)]:
        #             return False
        #         row[r].add(board[r][c])
        #         col[c].add(board[r][c])
        #         square[(r // 3, c // 3)].add(board[r][c])
        # return True

