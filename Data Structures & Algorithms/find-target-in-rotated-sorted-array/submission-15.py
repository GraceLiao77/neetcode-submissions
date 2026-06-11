class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        # nums=[4,5,6,7,0,1,2] target=0
        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m
            
            # check m in the sorted
            if nums[l] <= nums[m]:
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            # m in the un-sorted side
            else:
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        return -1

            
