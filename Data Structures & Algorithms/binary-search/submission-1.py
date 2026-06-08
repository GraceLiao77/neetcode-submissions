class Solution:
    def search(self, nums: List[int], target: int) -> int:
        length = len(nums)
        l = 0
        r = length - 1

        while l <= r:
            half_l = (r+l) // 2
            print(half_l)
            if nums[half_l] < target:
                l = half_l + 1
            elif nums[half_l] > target:
                r = half_l - 1
            else:
                return half_l
        return -1

        