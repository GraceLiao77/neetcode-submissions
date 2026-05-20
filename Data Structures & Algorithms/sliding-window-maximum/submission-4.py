class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1: return nums
        l = 0
        r = l + k - 1
        finalRes = []
        countMap = {}
        curMax = float('-infinity')
        for i in nums[l: r + 1]:
            curMax = max(curMax, i)
            countMap[i] = 1 + countMap.get(i, 0)
        finalRes.append(curMax)
        while r < len(nums) - 1:
            countMap[nums[l]] -= 1
            if countMap[nums[l]] == 0:
                del countMap[nums[l]]
            l += 1
            r += 1
            countMap[nums[r]] = 1 + countMap.get(nums[r], 0)
            if nums[l-1] != curMax:
                curMax = max(curMax, nums[r])
            else:
                if nums[l-1] not in countMap:
                    curMax = max(countMap)
                else:
                    curMax = max(curMax, nums[r])
            finalRes.append(curMax)
        return finalRes




        