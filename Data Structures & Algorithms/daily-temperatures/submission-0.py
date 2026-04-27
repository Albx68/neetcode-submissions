class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        l = len(temperatures)
        res = [0] * l
        stack = []

        for i,t in enumerate(temperatures):
            while stack and t>stack[-1][0]:
                _,j = stack.pop()
                res[j] = i-j
            stack.append([t,i])
        return res 