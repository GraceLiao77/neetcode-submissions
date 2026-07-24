class Solution:
    def hasDuplicate(self, nums: List[int]):
        res = list(dict.fromkeys(nums))
        print(res, len(res), len(nums))
        if len(res) == len(nums):
            return False
        return True

        

        