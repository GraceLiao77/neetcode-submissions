class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 1, 2, 4, 6 -> pre  1, 1, 2, 8 
        leftProduct = []
        lres = 1
        for i, item in enumerate(nums):
            if i == 0:
                leftProduct.append(1)
            else:
                lres = lres * nums[i-1]
                leftProduct.append(lres)
        rightProduct = []
        rres = 1
        newNums = nums[::-1]
        for i, item in enumerate(newNums):
            if i == 0:
                rightProduct.append(1)
            else:
                rres = rres * newNums[i-1]
                rightProduct.append(rres)
        rightProduct = rightProduct[::-1]
        res = []
        print(leftProduct, rightProduct, newNums)
        for i in range(len(leftProduct)):
            res.append(leftProduct[i] * rightProduct[i])
        return res


        