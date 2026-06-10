class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        if nums[l] > nums[r]:
            while l < r:
                mid = (l + r) // 2
                if nums[mid] < nums[mid + 1] and nums[mid] < nums[mid - 1]:
                    return nums[mid]
                else:
                    if nums[mid] > nums[r]:
                        l = mid + 1
                    else:
                        r = mid
            return nums[l]
        else:
            return nums[0]