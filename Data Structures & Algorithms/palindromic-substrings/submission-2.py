class Solution:
    def countSubstrings(self, s: str) -> int:
        # # dp
        # n = len(s)
        # dp = [[False] * n for _ in range(n)]
        # reslen = 0

        # for i in range(n-1, -1, -1):
        #     # i -> 3, 2, 1, 0
        #     for j in range(i, n):
        #         # j -> 3 | 2,3 | 1,2,3 | 0,1,2,3
        #         if s[i] == s[j] and (j-i+1 <= 3 or dp[i+1][j-1]):
        #             dp[i][j] = True
        #             reslen += 1
        # return reslen

        # two pointer
        count = 0
        n = len(s)
        for i in range(n):
            # odd
            l=r=i
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
                count += 1
            # even
            l, r = i, i+1
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
                count += 1
        return count
