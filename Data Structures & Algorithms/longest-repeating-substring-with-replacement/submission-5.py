class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen = defaultdict(int)
        l = 0
        r = 0
        maxfrenquent = 0
        maxres = 0
        while r <= (len(s) - 1):
            seen[s[r]] += 1
            maxfrenquent = max(seen.values())
            if r-l+1-maxfrenquent <= k:
                maxres = max(r-l+1, maxres)
                print('if maxres:', maxres, 'seen:',seen, 'l:',l, 'r:',r, 'maxfrenquent:',maxfrenquent)
                r += 1
            else:
                seen[s[l]] -= 1
                print('el maxres:', maxres, 'seen:',seen, 'l:',l, 'r:',r, 'maxfrenquent:',maxfrenquent)
                l += 1
                r += 1
        return maxres
            