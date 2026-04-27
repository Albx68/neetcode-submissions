class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = [(math.sqrt(pow(x-0,2)+pow(y-0,2)),i) for i,[x,y] in enumerate(points)]
        heapq.heapify(distances)
        res = []
        while k:
            _, index = heapq.heappop(distances)
            res.append(points[index])
            k-=1
        return res
        return [point for _,point in max_heap]