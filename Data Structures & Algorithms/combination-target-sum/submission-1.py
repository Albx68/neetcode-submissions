class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []

        def dfs(i,s,comb):
            if s == target:
                res.append(comb.copy())
                return
            if i>=len(nums)or s>target:
                return
            comb.append(nums[i])
            dfs(i,s+nums[i],comb)
            comb.pop()
            dfs(i+1,s,comb)
        dfs(0,0,[])
        return res
