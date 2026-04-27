class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        time = 0
        fresh = 0
        q = deque()
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    fresh+=1
                elif grid[r][c] == 2:
                    q.append([r,c])
        def checkbounds(r,c):
            if r<0 or c<0 or r>=m or c>=n:
                return False
            return True
        if fresh == 0:
            return 0
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        while q:
            for _ in range(len(q)):
                [r,c] = q.popleft()
                for d in directions:
                    [rd,cd] = d
                    newR,newC = r+rd,c+cd
                    
                    if checkbounds(newR,newC) and grid[newR][newC]==1:
                        grid[newR][newC] = 2
                        q.append([newR,newC])
                        fresh-=1

            time+=1
        print("fresh",fresh)
        return time-1 if fresh == 0 else -1
