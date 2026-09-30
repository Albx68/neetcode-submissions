class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0]*n for _ in range(m)]

        for r in range(m):
            dp[r][0] = 1
        for c in range(n):
            dp[0][c] = 1

        for r in range(1,m):
            for c in range(1,n):
                dp[r][c] = dp[r-1][c] + dp[r][c-1]
        
        return dp[m-1][n-1]
        # cache = {}
        # def checkbounds(r,c):
        #     if r>=m or c>=n:
        #         return False
        #     return True

        # def dfs(r,c):
        #     if not checkbounds(r,c):
        #         return 0
        #     if r == m-1 and c == n-1:
        #         return 1
        #     if (r,c) in cache:
        #         return cache[(r,c)]
        #     cache[(r,c)] = dfs(r+1,c) + dfs(r,c+1)
        #     return cache[(r,c)]
        # return dfs(0,0)