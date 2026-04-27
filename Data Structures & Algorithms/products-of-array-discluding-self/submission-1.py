class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        finalProduct = 1
        numOfZero = 0
        for i in nums:
            if i != 0:
                finalProduct *= i
            else:
                numOfZero += 1
        res = []
        # numOfZero = 1, finalProduct = -6
        for n in nums:
            if n != 0:
                if numOfZero == 0:
                    res.append(int(finalProduct/n))
                else:
                    res.append(0)
            elif n == 0:
                if numOfZero > 1:
                    res.append(0)
                else:
                    res.append(finalProduct)
        return res
        