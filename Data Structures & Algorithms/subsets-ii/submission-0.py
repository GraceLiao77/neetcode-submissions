class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        subset = []

        def dfs(i):
            if i == len(nums):
                res.append(subset[:])
                return
            # choice
            subset.append(nums[i])
            dfs(i+1)
            # undo
            while i < len(nums) - 1 and nums[i] == nums[i+1]:
                i += 1
            subset.pop()
            dfs(i+1)
        dfs(0)
        return res