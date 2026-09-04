class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 持有股票（今天买入了，或者之前买了还没卖）
        # 不持有股票，且不在冷冻期（可以买入）
        # 不持有股票，且在冷冻期（今天刚卖出，明天不能买）
        # hold[i]   = 第 i 天结束后，持有股票的最大利润
        # rest[i]   = 第 i 天结束后，不持有股票且不在冷冻期的最大利润
        # sold[i]   = 第 i 天结束后，不持有股票且处于冷冻期的最大利润（今天刚卖出）
        pl = len(prices)
        hold = [0] * pl
        rest = [0] * pl
        sold = [0] * pl

        hold[0] = -prices[0]
        rest[0] = 0
        sold[0] = float('-inf')

        for i in range(1, pl):
            # 持有：之前持有不动，或从休息状态买入
            hold[i] = max(hold[i-1], rest[i-1] - prices[i])
            
            # 卖出：从持有状态卖出
            sold[i] = hold[i-1] + prices[i]
            
            # 休息：从卖出状态冷冻结束，或继续休息
            rest[i] = max(rest[i-1], sold[i-1])
        
        # 最后一天不持有股票利润更大（持有股票还没卖）
        return max(sold[-1], rest[-1])
