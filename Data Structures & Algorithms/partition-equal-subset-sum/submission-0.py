class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
       
        total = sum(nums)
        if total % 2 == 1:
            return False
        target = total//2
        n = len(nums)
        # memo = {}
        memo = [[-1 for _ in range(target + 1)] for _ in range(len(nums))]


        def dfs(i,currsum):
            if currsum == target:
                return True
            if i >= n or currsum > target:
                return False
            if memo[i][currsum] != -1:
                return memo[i][currsum]
            
            include = dfs(i+1,currsum+nums[i])
            exclude = dfs(i+1,currsum)
            memo[i][currsum] = include or exclude
            return memo[i][currsum]

        return dfs(0,0)
