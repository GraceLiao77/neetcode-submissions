class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        subset = []
        def dfs(i, total):
            if total == target:
                res.append(subset[:])
                return
            if i == len(candidates) or total > target:
                return
            total += candidates[i]
            subset.append(candidates[i])
            dfs(i+1, total)
            while i < len(candidates)-1 and candidates[i] == candidates[i+1]:
                i += 1
            total -= candidates[i]
            subset.pop()
            dfs(i+1, total)
        dfs(0, 0)
        return res