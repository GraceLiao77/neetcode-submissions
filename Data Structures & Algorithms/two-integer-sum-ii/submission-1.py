class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # O(n) O(1)
        l, r = 0, len(numbers) - 1
        while l < r:
            curres = numbers[l] + numbers[r]
            if curres == target:
                return [l+1, r+1]
            elif curres < target:
                l += 1
            else:
                r -= 1
        return []



        
        # O(n2) O(1)
        # res = []
        # for i, num in enumerate(numbers):
        #     mins = target - num
        #     if mins in numbers:
        #         curIdx = numbers.index(mins)
        #         if i < curIdx:
        #             res.append(i+1)
        #             res.append(curIdx+1)
        #         else:
        #             return res
        #     else:
        #         continue
        # return res
