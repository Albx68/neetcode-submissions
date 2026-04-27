class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        res = 0
        while r<len(prices):
            profit = prices[r]-prices[l]
            res = max(res,profit)
            if prices[r] < prices[l]:
                l+=1
            else:
                r+=1
        return res