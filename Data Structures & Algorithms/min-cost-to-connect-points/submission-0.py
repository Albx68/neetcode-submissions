class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        N = len(points)
        adj = {i:[] for i in range(N)}

        for i in range(N):
            x1,y1 = points[i]
            for j in range(i+1,N):
                x2,y2 = points[j]
                dst = abs(x1-x2) + abs(y1-y2)
                adj[i].append([dst,j])
                adj[j].append([dst,i])
        
        visited = set()
        minheap = [[0,0]]
        res = 0
        while len(visited) < N:
            currCost,i = heapq.heappop(minheap)
            if i in visited:
                continue
            res += currCost
            visited.add(i)

            for neiCost,nei in adj[i]:
                if nei not in visited:
                    heapq.heappush(minheap,[neiCost,nei])
        return res