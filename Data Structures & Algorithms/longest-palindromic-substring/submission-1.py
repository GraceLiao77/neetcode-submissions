class Solution:
    def longestPalindrome(self, s: str) -> str:
        reslen = 0
        resIdx = 0
        # only concentrate on 上三角，因为下三角是s[3..1]这种从idx 3->1 逆序不存在这种字串
        n = len(s)
        dp = [[False] * n for _ in range(len(s))]
        # because dp[i][j] rely on dp[i+1][j-1] result, so we should run i from right to left. run j from left to right
        # 3,3 2,2 2,3 1,1 1,2 1,3
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j-i+1 <= 3 or dp[i+1][j-1]):
                    dp[i][j] = True
                    if j-i+1 > reslen:
                        reslen = j-i+1
                        resIdx = i
        return s[resIdx: resIdx+reslen]


        

        # for i in range(len(s)):
        #     # odd 'aba'
        #     l = r = i
        #     while l >= 0 and r < len(s) and s[l] == s[r]:
        #         if r - l +1 > reslen:
        #             resIdx = l
        #             reslen = r - l +1
        #         l -= 1
        #         r += 1

        #     # even 'abba'
        #     l, r = i, i+1
        #     while l >= 0 and r < len(s) and s[l] == s[r]:
        #         if r - l +1 > reslen:
        #             resIdx = l
        #             reslen = r - l +1
        #         l -= 1
        #         r += 1
        # return s[resIdx:resIdx+reslen]