class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        finalBool = True
        # row
        for row in board:
            res = set()
            for item in row:
                if item == ".":
                    continue
                elif item not in res:
                    res.add(item)
                else:
                    finalBool = False
                    return finalBool
        # col
        arrlen = len(board[0])
        for i, item in enumerate(board):
            index = 0
            res = set()
            while index <= arrlen-1:
                curitem = board[index][i]
                index += 1
                if curitem == ".":
                    continue
                elif curitem not in res:
                    res.add(curitem)
                else:
                    finalBool = False
                    return finalBool
        # 3x3
        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square // 3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    elif board[row][col] not in seen:
                        seen.add(board[row][col])
                    else:
                        finalBool = False
                        return finalBool
        return finalBool
        




        