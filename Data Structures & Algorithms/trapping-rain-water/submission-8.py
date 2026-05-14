class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        lmax = height[l]
        r = len(height) - 1
        rmax = height[r]
        finalwater = 0
        while l < r:
            lmax = max(lmax, height[l])
            rmax = max(rmax, height[r])
            if height[l] < height[r]:
                cur = min(lmax, rmax) - height[l]
                l += 1
            else:
                cur = min(lmax, rmax) - height[r]
                r -= 1
            if cur >= 0:
                finalwater += cur
        return finalwater
           

        # left = [0]
        # right = [0]
        # water = []
        # reverseHeigh = height[::-1]

        # for i in height:
        #     if left[-1] >= i:
        #         left.append(left[-1])
        #     else:
        #         left.append(i)
        # for r in reverseHeigh:
        #     if right[-1] >= r:
        #         right.append(right[-1])
        #     else:
        #         right.append(r)
        # print(left, right)
        # right = right[::-1]
        # for idx, item in enumerate(height):
        #     store = min(left[idx], right[idx]) - item
        #     if store >= 0:
        #         water.append(store)
        #     else:
        #         water.append(0)
        # finalres = 0
        # for w in water:
        #     finalres += w
        # return finalres
