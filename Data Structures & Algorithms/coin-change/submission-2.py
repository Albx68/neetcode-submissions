class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        res = float('inf')
        cache = set()
        def dp(i,curr,count):
            nonlocal res
            if (i,curr,count) in cache:
                return
            if i>=len(coins):
                return 
            
            if curr>amount:
                return 
            
            if curr == amount:
                res = min(res,count)
                return 
            cache.add((i,curr,count))
            dp(i,curr+coins[i],count+1)
            dp(i+1,curr,count)
        dp(0,0,0)
        return res if res != float('inf') else -1
