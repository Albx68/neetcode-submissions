class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows,cols = len(board),len(board[0])
        directions = [(-1,0),(1,0),(0,1),(0,-1)]

        def checkBounds(r,c):
            if r<0 or c<0 or r>=rows or c>=cols:
                return False
            return True

        def capture(r,c):
            if not checkBounds(r,c) or board[r][c]!= "O":
                return 
            board[r][c] = 'T'
            for dr,dc in directions:
                capture(r+dr,c+dc)


        for r in range(rows):
            if board[r][0] == "O":
                capture(r,0)
            if board[r][cols-1] == "O":
                capture(r,cols-1)
        
        for c in range(cols):
            if board[0][c] == "O":
                capture(0,c)
            if board[rows-1][c] == "O":
                capture(rows-1,c)
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"
        
        