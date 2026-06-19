class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        mapnums = {}

        for i in nums:
            if i in mapnums:
                return i
            else:
                mapnums[i] = True
        return -1