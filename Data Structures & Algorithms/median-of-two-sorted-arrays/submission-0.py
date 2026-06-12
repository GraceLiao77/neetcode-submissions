class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        half = total // 2
        # nums1 less than nums2
        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1
        
        l, r = 0, len(nums1) - 1
        # []
        # [1,2,3,5,5,6,7,8,9,10]
        # total = 10 half = 5
        while True:
            m = (l + r) // 2
            rest = half - (m + 1) - 1
            Aleft = nums1[m] if m >= 0 else float("-inf")
            Aright = nums1[m+1] if (m + 1) < len(nums1) else float("inf")
            Bleft = nums2[rest] if (rest) >= 0 else float("-inf")
            Bright = nums2[rest+1] if (rest+1) < len(nums2) else float("inf")
            if Aleft <= Bright:
                if Bleft <= Aright:
                    if total % 2 == 0:
                        return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
                    else:
                        return min(Aright, Bright)
                else:
                    l = m + 1
            else:
                r = m - 1