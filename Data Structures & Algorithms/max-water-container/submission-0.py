class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        l,r = 0, n-1
        maxVal = float('-inf')
        while l<r:
            minh = min(heights[l],heights[r])
            width = (r) - (l)
            vol = minh*width
            maxVal = max(vol,maxVal)
            if heights[l]<= heights[r]:
                l+=1
            else:
                r-=1
        return maxVal