class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
         # que = {
            #     16: 5 -> 15 14 13 12 11
            #     17: 1,
            #     18: 6
            # }
        que = defaultdict(int)
        res = 0
        for num in set(nums):
            que[num] = 1 + que[num - 1] + que[num + 1]
            # refresh start point should set que[num]
            que[num - que[num - 1]] = que[num]
            # refresh end point should set que[num]
            que[num + que[num + 1]] = que[num]
            res = max(res, que[num])
        return res


        # arr = set(nums)
        # res = 0
        # for i in nums:
        #     if (i-1) not in nums: # arr[i] is start point
        #         length = 1
        #         n = 1
        #         while (i+n) in nums:
        #             length += 1
        #             n += 1
        #         res = max(res, length)
        # return res


        