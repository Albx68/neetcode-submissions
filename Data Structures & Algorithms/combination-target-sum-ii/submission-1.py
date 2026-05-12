class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        candidates.sort()

        def dfs(i,s,curr):
            if s == target :
                res.append(curr.copy())
                return
            if i>= len(candidates) or s > target:
                return

            curr.append(candidates[i])
            dfs(i+1,s+candidates[i],curr)
            curr.pop()

            while i+1<len(candidates) and candidates[i]==candidates[i+1]:
                i+=1
                
            dfs(i+1,s,curr)

        dfs(0,0,[])
        return res