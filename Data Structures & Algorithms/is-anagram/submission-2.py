class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        smap = Counter(s)
        tmap = Counter(t)

        for c in s:
            if smap.get(c) != tmap.get(c):
                return False
        return True