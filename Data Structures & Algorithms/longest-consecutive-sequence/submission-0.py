class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        arr = set(nums)
        res = 0
        for i in nums:
            if (i-1) not in nums: # arr[i] is start point
                length = 1
                n = 1
                while (i+n) in nums:
                    length += 1
                    n += 1
                res = max(res, length)
        return res


        