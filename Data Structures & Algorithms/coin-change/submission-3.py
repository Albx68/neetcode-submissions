class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        cache = {}
        def dfs(left):
            if left in cache:
                return cache[left]
            if left == 0:
                return 0
            res = float('inf')
            for c in coins:
                if left - c >=0:
                    res = min(res, 1+dfs(left-c))
            cache[left] = res
            return cache[left]
        
        mincoins = dfs(amount)
        return -1 if mincoins == float('inf') else mincoins
