class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        pacific = set()
        atlantic = set()
        # for r in range(rows):
        #     pacific.add((r,0)) 
        #     atlantic.add((r,cols-1))
        # for c in range(cols):
        #     atlantic.add((rows-1,c))
        #     pacific.add((0,c)) 
        
        def checkBounds(r,c):
            if r<0 or c<0 or r>= rows or c>=cols:
                return False
            else:
                return True
        directions = [(-1,0),(1,0),(0,1),(0,-1)]
        def dfs(r,c,visited,prev):
            if not checkBounds(r,c): return
            if (r,c) in visited: return
            if heights[r][c] < prev: return
            newPrev = heights[r][c]
            visited.add((r,c))
            for dr,dc in directions:
                dfs(r+dr,c+dc,visited,newPrev)
        for c in range(cols):
            dfs(0, c, pacific, heights[0][c])
            dfs(rows - 1, c, atlantic, heights[rows - 1][c])
        for r in range(rows):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, cols - 1, atlantic, heights[r][cols - 1])
        res = []
        for r in range(rows):
            for c in range(cols):
                if (r,c) in atlantic and (r,c) in pacific:
                    res.append(([r,c]))
        return res
        
