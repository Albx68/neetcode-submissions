class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1
        collen = len(matrix[0]) - 1
        targetrow = None
        while l<=r:
            midrow = (l+r)//2
            if matrix[midrow][0] == target or matrix[midrow][collen] == target:
                return True
            if matrix[midrow][0] > target:
                r = midrow - 1
            elif matrix[midrow][0]< target and matrix[midrow][collen] > target:
                targetrow = matrix[midrow]
                break
            else:
                l = midrow+1
        
        targetrowl =0
        if not targetrow:
            return False

        targetrowr = len(targetrow)-1

        while targetrowl<=targetrowr:
            targetmid = (targetrowl+targetrowr)//2
            if targetrow[targetmid] == target:
                return True
            if targetrow[targetmid] > target:
                targetrowr = targetmid - 1
            else:
                targetrowl = targetmid + 1
        return False


