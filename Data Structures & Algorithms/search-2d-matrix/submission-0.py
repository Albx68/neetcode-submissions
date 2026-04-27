class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        def findTargetRow():
            for i in range(rows):
                if matrix[i][0] <= target and matrix[i][cols-1]>=target:
                    return i
            return -1
        
        targetRow = findTargetRow()

        if targetRow == -1:
            return False
        
        def bs(low,high):
            if low>high:
                return False
            mid = low + (high-low)//2
            midVal = matrix[targetRow][mid]
            if midVal == target:
                return True
            if midVal < target:
                return bs(mid+1,high)
            else:
                return bs(low,mid-1)
        return bs(0,cols-1)