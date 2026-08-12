class Solution:
    def rob(self, nums: List[int]) -> int:
        # rob1 steal cur rob2 don't steal cur
        rob1, rob2 = 0, 0
        for i in nums:
            temp = max(i+rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2

        # cache = {}
        # def dfs(i):
        #     if i >= len(nums):
        #         return 0
        #     if i in cache:
        #         return cache[i]
        #     # rob this one
        #     cache[i] = max(nums[i] + dfs(i+2), dfs(i+1))
        #     return cache[i]

        # return dfs(0)