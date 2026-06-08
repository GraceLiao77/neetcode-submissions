class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # brute force
        l = len(heights)
        max_area = 0

        for i in range(l):
            min_height = heights[i]
            for j in range(i, l):
                min_height = min(heights[j], min_height)
                max_area = max(max_area, (j-i+1) * min_height)
        return max_area