class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ''
        for i in strs:
            s += str(len(i))+'#'+ i
        return s
    def decode(self, s: str) -> List[str]:
        # 2#hi5#Grace
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            l = int(s[i:j])
            res.append(s[j+1:j+l+1])
            i = j+l+1
        return res
