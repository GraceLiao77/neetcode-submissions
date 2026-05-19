class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t): return ''

        countT, window = {}, {}
        
        for i in t:
            countT[i] = 1 + countT.get(i, 0)
        
        have, need = 0, len(countT)
        shortres, shortlen = [-1, -1], float('infinity')

        l = 0
        for r in range(len(s)):
            print(r, )
            window[s[r]] = 1 + window.get(s[r], 0)
            if s[r] in t and window[s[r]] == countT[s[r]]:
                have += 1
            
            while have == need:
                if r - l + 1 < shortlen:
                    shortlen = r - l + 1
                    shortres = [l, r]
                if s[l] in t:
                    window[s[l]] -= 1
                    if window[s[l]] < countT[s[l]]: 
                        have -= 1
                l += 1
        return s[shortres[0]:shortres[1]+1]
