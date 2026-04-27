class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = {}
        for n in nums:
            count[n] = 1+count.get(n,0)
        for value in count.values():
            if value > 1:
                return True
        return False