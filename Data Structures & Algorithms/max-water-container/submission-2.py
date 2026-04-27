class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0,len(heights) - 1
        res = 0
        while l<r:
            lheight = heights[l]
            rheight = heights[r]
            area = min(lheight,rheight) * (r-l)
            res = max(res,area)
            if lheight > rheight:
                r-=1
            else:
                l+=1
        return res