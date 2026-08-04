class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mapList = defaultdict(int)
        maxnum = 0
        for i in nums:
            if not mapList[i]:
                mapList[i] = mapList[i-1] + mapList[i+1] + 1
                mapList[i - mapList[i-1]] = mapList[i]
                mapList[i + mapList[i+1]] = mapList[i]
                maxnum = max(maxnum, mapList[i])
        return maxnum


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


        