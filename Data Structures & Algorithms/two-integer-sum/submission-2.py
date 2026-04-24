class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        resmap = {}
        for i, item in enumerate(nums):
            final = target - item
            if final in resmap:
                return [resmap[final], i]
            resmap[item] = i
           
        
        