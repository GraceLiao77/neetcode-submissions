class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        res = list(zip(position, speed))
        res.sort(reverse = True)
        # [(7,1), (4,2), (1,2), (0,1)]
        stack = [] # last-in first-out

        for p, s in res:
            time = (target - p) / s

            if not stack or time > stack[-1]:
                stack.append(time)
        return len(stack)





