class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        order_s = "".join(sorted(s))
        order_t = "".join(sorted(t))
        index = 0

        for i in order_s:
            if i != order_t[index]:
                return False
            else:
                index += 1
                continue
        return True