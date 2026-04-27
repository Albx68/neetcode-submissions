class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        res,l,r = 0,0,len(people)-1
        people.sort()

        while l<=r:
            remaining = limit - people[r]
            res+=1
            r-=1
            if l<=r and remaining>=people[l]:
                l+=1
        return res