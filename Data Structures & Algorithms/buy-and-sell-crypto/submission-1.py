class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        res = 0
        while r <= (len(prices) - 1):
            curprofit = prices[r] - prices[l]
            res = max(res, curprofit)
            if prices[r] < prices[l]:
                l = r
            r += 1 
            

        return res