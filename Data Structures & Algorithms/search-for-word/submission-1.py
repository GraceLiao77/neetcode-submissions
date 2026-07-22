class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rlen = len(board)
        clen = len(board[0])

        def dfs(r_idx, c_idx, word_idx): # row, col, word item position
            # is finished?
            if word_idx == len(word):
                return True
            # can i keep going?
            # out of range | unequal val | mark to used
            if (r_idx < 0 or r_idx > rlen-1 or c_idx < 0 or c_idx > clen-1) or (
                board[r_idx][c_idx] != word[word_idx]
            ) or (board[r_idx][c_idx] == '#'):
                return False
            
            board[r_idx][c_idx] = '#'
            if dfs(r_idx-1,c_idx,word_idx+1) or dfs(r_idx+1,c_idx,word_idx+1) or dfs(r_idx,c_idx-1,word_idx+1) or dfs(r_idx,c_idx+1,word_idx+1):
                return True
            board[r_idx][c_idx] = word[word_idx]
        # every cell will be a strat point
        for r in range(rlen):
            for c in range(clen):
                if dfs(r, c, 0):
                    return True
        return False

