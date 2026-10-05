class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]


        for i in range(m):
            for j in range(n):

                if text1[i] == text2[j]:
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = 1 + dp[i-1][j-1]

                else:
                    if i == 0 and j == 0:
                        dp[i][j] = 0
                    elif i == 0:
                        dp[i][j] = dp[i][j-1]
                    elif j == 0:
                        dp[i][j] = dp[i-1][j]
                    else:
                        dp[i][j] = max(
                            dp[i-1][j],
                            dp[i][j-1]
                        )

        return dp[m-1][n-1]