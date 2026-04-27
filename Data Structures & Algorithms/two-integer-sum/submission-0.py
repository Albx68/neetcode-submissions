class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        for i in range(len(nums)):
            n = nums[i]
            diff = target - n
            if diff in m:
                return [m[diff],i]
            m[n] = i
        