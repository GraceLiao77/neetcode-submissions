class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # hashmap
        if len(s) != len(t):
            return False
        new_map = {}
        for i in range(len(s)):
            new_map[s[i]] = new_map.get(s[i], 0) + 1
            new_map[t[i]] = new_map.get(t[i], 0) - 1
        
        return all(v == 0 for v in new_map.values())

        # if len(s) != len(t):
        #     return False
        # order_s = "".join(sorted(s))
        # order_t = "".join(sorted(t))
        # index = 0

        # for i in order_s:
        #     if i != order_t[index]:
        #         return False
        #     else:
        #         index += 1
        #         continue
        # return True