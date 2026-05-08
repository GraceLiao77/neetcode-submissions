class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        lHeight = 0
        rHeight = len(heights) - 1
        while lHeight < rHeight:
            width = rHeight - lHeight
            res = max(res, min(heights[lHeight] * width, heights[rHeight] * width))
            if heights[lHeight] < heights[rHeight]:
                lHeight += 1
            elif heights[lHeight] > heights[rHeight]:
                rHeight -= 1
            else:
                lHeight += 1
                rHeight -= 1
        return res
