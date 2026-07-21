class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        used = [False] * len(nums)

        # i is 填 permutation 的第几个位置
        def dfs(i):
            # stop
            if i == len(nums):
                res.append(subset[:])
                return
            # Traverse all numbers, skip used ones
            for j in range(len(nums)):
                if used[j]:
                    continue
                # choice
                subset.append(nums[j])
                used[j] = True
                dfs(i + 1)
                # undo
                subset.pop()
                used[j] = False
        dfs(0)
        return res