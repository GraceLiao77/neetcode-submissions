class Solution:
    def hasDuplicate(self, nums: List[int]):
        set_nums = set(nums[:])
        if len(set_nums) < len(nums):
            return True
        else:
            return False

        

        