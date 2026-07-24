class Solution:
    def hasDuplicate(self, nums: List[int]):
        res = set()
        for i in nums:
            if i in res:
                return True
            res.add(i)
        return False

        # # res = list(dict.fromkeys(nums))
        # res = set(nums)
        # if len(res) == len(nums):
        #     return False
        # return True

        

        