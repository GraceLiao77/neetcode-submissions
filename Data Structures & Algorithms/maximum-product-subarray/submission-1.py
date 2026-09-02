class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # optimism space
        if not nums:
            return 0
        dp_max = dp_min = nums[0]
        res = nums[0]
        for i in range(1, len(nums)):
            pre_max = dp_max
            pre_min = dp_min
            dp_max = max(pre_max * nums[i], pre_min * nums[i], nums[i])
            dp_min = min(pre_max * nums[i], pre_min * nums[i], nums[i])
            res = max(dp_max, res)
        return res

        # if not nums:
        #     return 0
        # dp_max = [0] * len(nums)
        # dp_min = [0] * len(nums)
        # dp_max[0] = dp_min[0] = nums[0]

        # for i in range(1, len(nums)):
        #     dp_max[i] = max(nums[i], dp_max[i-1] * nums[i], dp_min[i-1]*nums[i])
        #     dp_min[i] = min(nums[i], dp_max[i-1] * nums[i], dp_min[i-1]*nums[i])

        # return max(dp_max)


