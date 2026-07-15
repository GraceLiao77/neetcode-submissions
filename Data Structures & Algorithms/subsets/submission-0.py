class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        sublist = []

        def dfs(i):
            if i >= len(nums):
                res.append(sublist[:])
                return
            sublist.append(nums[i])
            dfs(i + 1)

            sublist.pop()
            dfs(i + 1)

        dfs(0)    
        return res