# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        res = 0
        def count(node,maxsofar):
            nonlocal res
            if not node:
                return 
            if node.val >= maxsofar:
                res+=1
            newmax = max(maxsofar,node.val)
            
            count(node.left,newmax)
            count(node.right,newmax)
        count(root,float('-inf'))
        return res