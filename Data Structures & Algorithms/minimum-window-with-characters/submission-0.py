class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ''
        need = Counter(t)
        window = {}

        required = len(need)
        formed = 0

        bestleft = 0
        minlength = float('inf')

        l,r = 0,0

        while r<len(s):
            char = s[r]
            window[char] = window.get(char,0)+1

            if char in need and window[char] == need[char]:
                formed+=1
            
            while l<=r and formed == required:
                leftchar = s[l]
                if r-l+1 < minlength:
                    bestleft = l
                    minlength = r-l+1
                window[leftchar]-=1

                if leftchar in need and window[leftchar] < need[leftchar]:
                    formed-=1
                l+=1
            r+=1
        return '' if minlength == float('inf') else s[bestleft:bestleft+minlength]
