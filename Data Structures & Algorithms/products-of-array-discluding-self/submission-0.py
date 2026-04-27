class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        pref = 1
        n = len(nums)
        res = [0]*n
        for i in range(n):
            res[i] = pref
            pref*= nums[i]
        post = 1
        for i in range(len(nums)-1,-1,-1):
            res[i] *= post
            post*=nums[i]
        return res
        