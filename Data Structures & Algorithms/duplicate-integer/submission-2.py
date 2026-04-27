class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numset = set(nums)
        return not len(numset) == len(nums)