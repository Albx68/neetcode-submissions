class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        scount = Counter(s)
        tcount = Counter(t)

        for c in s:
            if c not in tcount:
                return False
            if scount[c] != tcount[c]:
                return False
        
        return True