class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [(0,0)] * len(nums)
        for i in range(0, len(nums)):
            dp[i] = (1, nums[i]) #(len, max_item)
        res = 1
        for i in range(1, len(nums)):
            pre = dp[i]
            for l,m in dp[:i]:
                if nums[i] > m and l+1 > pre[0]:
                    dp[i] = (l+1, nums[i])
                    pre = max(pre, dp[i])
                    res = max(l+1, res)
        print(dp)
        return res