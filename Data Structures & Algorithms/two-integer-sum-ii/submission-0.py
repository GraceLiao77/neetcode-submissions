class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = []
        for i, num in enumerate(numbers):
            mins = target - num
            if mins in numbers:
                curIdx = numbers.index(mins)
                if i < curIdx:
                    res.append(i+1)
                    res.append(curIdx+1)
                else:
                    return res
            else:
                continue
        return res
