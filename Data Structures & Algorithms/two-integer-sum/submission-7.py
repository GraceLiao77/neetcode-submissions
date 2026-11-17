class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for idx, num in enumerate(nums):
        #     res = target - num
        #     for i, n in enumerate(nums[idx+1:]):
        #         if n == res:
        #             return [idx, i+1+idx]
        # return []
        
        reslist = dict({})
        for idx, num in enumerate(nums):
            res = target - num
            if res in reslist:
                return [reslist[res], idx]
            else:
                reslist[num] = idx
        