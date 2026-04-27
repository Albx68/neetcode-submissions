class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        while l<r:

            m = (l+r)//2
            total = sum(math.ceil(p/m) for p in piles)
            if total <= h:
                r = m
            else:
                l = m+1
        return l