class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        maplist = {}
        for i, item in enumerate(nums):
            count = target - item
            if count in maplist:
                return [maplist[count], i]
            maplist[item] = i
        return []


        # res = []
        # maplist = {} # val -> idx
        # for i, item in enumerate(nums):
        #     maplist[item] = i
        # for idx, j in enumerate(nums):
        #     if target-j in maplist and idx != maplist[target-j]:
        #         return [idx, maplist[target-j]]

        # return res
           
        
        