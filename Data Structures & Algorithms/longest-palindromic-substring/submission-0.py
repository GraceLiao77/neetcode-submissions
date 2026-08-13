class Solution:
    def longestPalindrome(self, s: str) -> str:
        reslen = 0
        resIdx = 0

        for i in range(len(s)):
            # odd 'aba'
            l = r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l +1 > reslen:
                    resIdx = l
                    reslen = r - l +1
                l -= 1
                r += 1

            # even 'abba'
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l +1 > reslen:
                    resIdx = l
                    reslen = r - l +1
                l -= 1
                r += 1
        return s[resIdx:resIdx+reslen]