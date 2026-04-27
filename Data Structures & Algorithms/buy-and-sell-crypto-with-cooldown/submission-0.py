class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        memo = {}

        def dfs(i,canbuy):
            if i >= len(prices):
                return 0
            if (i,canbuy) in memo:
                return memo[(i,canbuy)]
            if canbuy:

                buy = dfs(i+1,False) - prices[i]
                skip = dfs(i+1,True)
                memo[(i,canbuy)]= max(buy,skip)
            
            else:

                sell = dfs(i+2,True) + prices[i]
                skip = dfs(i+1,False)
                memo[(i,canbuy)] = max(sell,skip)
            return memo[(i,canbuy)]

        
        return dfs(0,True)