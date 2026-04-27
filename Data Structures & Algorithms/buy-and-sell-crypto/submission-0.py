class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minVal = float("inf")
        res = 0
        for i in range(len(prices)):
            curr = prices[i]
            minVal = min(minVal,curr)
            res = max(res,curr-minVal)
        return res