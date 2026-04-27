class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = [] #pair: (index,height)
        for i,h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index,height = stack.pop()
                width = i - index
                maxArea = max(maxArea,height*width)
                start = index
            stack.append((start,h))
        for i,h in stack:
            width = len(heights) - i
            maxArea = max(maxArea,h*width)
        return maxArea