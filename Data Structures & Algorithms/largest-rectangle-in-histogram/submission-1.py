class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # stack - monotone increasing
        stack = []
        heights = [0] + heights + [0]
        max_area = 0
        for i, item in enumerate(heights):
            if not stack or heights[stack[-1]] < item:
                stack.append(i)
            else:
                while heights[stack[-1]] >= item:
                    cur = stack.pop()
                    if not stack:
                        break
                    left = stack[-1]
                    right = i
                    max_area = max(max_area, (right-left-1)*heights[cur])
                stack.append(i)
        return max_area

            

        # brute force
        # l = len(heights)
        # max_area = 0

        # for i in range(l):
        #     min_height = heights[i]
        #     for j in range(i, l):
        #         min_height = min(heights[j], min_height)
        #         max_area = max(max_area, (j-i+1) * min_height)
        # return max_area