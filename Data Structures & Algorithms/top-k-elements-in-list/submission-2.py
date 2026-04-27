class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        l = []
        for c in count:
            l.append((count[c],c))
        
        sortedl = sorted(l,key= lambda x:x[0] )
        res = []
        while len(res)<k:
            res.append(sortedl.pop()[1])
        return res