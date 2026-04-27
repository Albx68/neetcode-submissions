class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)
        maxCount = count[nums[0]]
        maxVal = nums[0]
        for k in count:
            if count[k] > maxCount:
                maxCount = count[k]
                maxVal = k
        return maxVal