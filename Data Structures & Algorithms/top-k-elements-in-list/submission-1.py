class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        #find most frequent element
        freq = {}
        for n in nums:
            freq[n] = 1+freq.get(n,0)
        sortedFreq = list(sorted(freq.items(), key=lambda item: item[1],reverse=True))
        print(sortedFreq)
        ans = []
        i = 0
        while k>0:
            curr = sortedFreq[i]
            ans.append(curr[0])
            i= i+1
            k=k-1
        return ans
        
       