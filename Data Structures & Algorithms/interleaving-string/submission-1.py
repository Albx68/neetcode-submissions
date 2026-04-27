class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m,n,o = len(s1),len(s2),len(s3)
        memo = {}

        def dfs(i,j,c):

            if c == o:
                return i == m and j == n
            
            if (i,j,c) in memo:
                return memo[(i,j,c)]
            res = False

            if i<m and s1[i] == s3[c]:
                res = res or dfs(i+1,j,c+1)
            if j<n and s2[j] == s3[c]:
                res = res or dfs(i,j+1,c+1)
            
            memo[(i,j,c)] = res
            return res
        return dfs(0,0,0)