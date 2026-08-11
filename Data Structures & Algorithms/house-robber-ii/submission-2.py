class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        cache = {}
        # don't rob the first
        a = nums[1:]
        # don't rob the last
        b = nums[:-1]

        def dfs(i, new_nums):
            if i >= len(new_nums):
                return 0
            if i not in cache:
                cache[i] = max(dfs(i+1, new_nums), new_nums[i] + dfs(i+2, new_nums))
            return cache[i]
        result_a = dfs(0, a)
        cache = {}
        result_b = dfs(0, b)

        return max(result_a, result_b)