class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s%2 != 0 :
            return False
        
        target = s//2
        cache = {}
        def dfs(i,curr):
            
            if (i,curr) in cache:
                return cache[(i,curr)]
            if i == len(nums) or curr > target:
                return False
            
            if curr == target:
                return True
            else:
                res =  dfs(i+1,curr+nums[i]) or dfs(i+1,curr)
                cache[(i,curr)] = res
                return res
        
        return dfs(0,0)
