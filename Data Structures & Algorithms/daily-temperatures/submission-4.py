class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # [index, temp]
        idx = len(temperatures) - 1

        # idx = 0 [[1, 38],[5, 40]]
        while idx >= 0:
            print(stack)
            if stack and stack[-1][1] <= temperatures[idx]:
                while stack and temperatures[idx] >= stack[-1][1]:
                    stack.pop()
            if stack:
                res[idx] = stack[-1][0] - idx
            stack.append((idx, temperatures[idx]))

            idx -= 1
        return res
