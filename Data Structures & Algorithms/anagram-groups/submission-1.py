class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = defaultdict(list)
        for s in strs:
            carr = [0]*26
            for c in s:
                carr[ord('a')-ord(c)] +=1
            m[tuple(carr)].append(s)
        
        return list(m.values())