class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        count = sum(nums)
        if count % 2 != 0:
            return False

        target = count // 2

        # 二维矩阵避免被重复使用，一维矩阵会出现重复使用的状态
        # dp[i][j] 代表，站在nums里的第i个元素前，能不能组合成j
        dp = [[False] * (target+1) for _ in range(len(nums)+1)]
        dp[0][0] = True

        for i in range(1, len(nums)+1):
            num = nums[i-1]
            for j in range(target+1):
                # pick i
                dp[i][j] = (j >= num and dp[i-1][j-num]) or dp[i-1][j]
                # # not pick i
                # dp[i][j] = dp[i-1][j]
        return dp[-1][-1]
