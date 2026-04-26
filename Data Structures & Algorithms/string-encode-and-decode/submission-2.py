class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs:
            res += str(len(i)) + "#" + i #not rely on # to split, just a signal
        return res

    def decode(self, s: str) -> List[str]:
        # 5#hello5#world
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            num = s[i:j]
            i = j + int(num) + 1
            res.append(s[j+1:i])
        return res

