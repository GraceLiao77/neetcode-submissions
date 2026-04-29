class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
    #    1, 2, 4, 6 -> pre  1, 1, 2, 8 
        res = []
        for i, item in enumerate(nums):
            if i == 0:
                res.append(1)
            else:
                res.append(nums[i-1] * res[i-1])
        print(res)
        after = 1
        newnums = nums[::-1]
        finalres = []
        for n, item in enumerate(newnums):
            if n == 0:
                after = 1
            else:
                after = after * newnums[n-1]
            print(after)
            finalres.append(after * res[len(res)-1-n])
        print(finalres)
        return finalres[::-1]



        