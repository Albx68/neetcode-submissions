
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        firstChar = word[0]
        m = len(board)
        n = len(board[0])

        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        def checkBounds(r,c):
            if r<0 or c<0 or r>= m or c>=n:
                return False
            return True

        def dfs(r,c,i):
            if i == len(word):
                return True
            if not checkBounds(r,c):
                return False
            if board[r][c] != word[i]:
                return False
            if board[r][c] == 'dum':
                return False
            temp = board[r][c]
            board[r][c] = 'dum'
            res = False
            for dr,dc in directions:
                if dfs(r+dr,c+dc,i+1):
                    res = True
                    break
            board[r][c] = temp
            return res

        for r in range(m):
            for c in range(n):
                if board[r][c] == firstChar:
                    if dfs(r,c,0):
                        return True
        return False

        