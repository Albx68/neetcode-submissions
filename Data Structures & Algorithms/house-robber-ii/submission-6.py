class Solution:
    def rob(self, nums: List[int]) -> int:
        
        cache = {}

        def dfs(i,flag):
            if len(nums) == 1:
                return nums[0]
            if (i>=len(nums)) or (i == len(nums)-1 and flag):
                return 0

            if (i,flag) in cache:
                return cache[(i,flag)]
            cache[(i,flag)] =  max(dfs(i+1,flag),nums[i]+dfs(i+2,flag or i == 0))
            return cache[(i,flag)]

        return max(dfs(0,True),dfs(1,False))