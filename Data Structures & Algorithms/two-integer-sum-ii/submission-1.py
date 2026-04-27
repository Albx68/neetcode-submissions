class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        l,r = 0,len(numbers)-1

        while l<r:
            leftval = numbers[l]
            rightval = numbers[r]
            total = leftval + rightval
            if total == target:
                return [l+1,r+1]
            if total > target:
                r-=1
            else:
                l+=1
        return -1