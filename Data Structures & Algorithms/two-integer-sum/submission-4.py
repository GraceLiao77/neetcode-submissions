class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        maplist = {} # val -> idx
        for i, item in enumerate(nums):
            maplist[item] = i
        for idx, j in enumerate(nums):
            if target-j in maplist and idx != maplist[target-j]:
                return [idx, maplist[target-j]]

        return res
           
        
        