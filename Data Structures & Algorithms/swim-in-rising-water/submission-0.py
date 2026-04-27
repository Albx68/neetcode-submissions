class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        minheap = [(grid[0][0],0,0)]
        distance = [[float('inf') for i in range(rows)] for j in range(cols)]
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        def checkbounds(r,c):
            if r<0 or r>=rows or c<0 or c>=cols:
                return False
            return True
        
        while minheap:
            currdist, i,j = heapq.heappop(minheap)
            if currdist > distance[i][j]:
                continue
            
            for dr,dc in directions:
                nr,nc = dr+i,dc+j

                if checkbounds(nr,nc):
                    newdist = max(currdist,grid[nr][nc])
                    if newdist < distance[nr][nc]:
                        distance[nr][nc] = newdist
                        heapq.heappush(minheap,(newdist,nr,nc))
                    if nr == rows-1 and nc == cols-1:
                        return newdist
        return grid[0][0]