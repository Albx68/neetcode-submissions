class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        cache = {}
        def dp(l,r):
            if l>=r:
                return True
            if s[l]!=s[r]:
                return False
            if (l,r) in cache:
                return cache[(l,r)]
            cache[(l,r)]= dp(l+1,r-1)
            return cache[(l,r)]

        
        for l in range(len(s)):
           for r in range(l,len(s)):
                if dp(l, r):
                    if (r - l + 1) > len(res):
                        res = s[l:r + 1]
        
        return res
