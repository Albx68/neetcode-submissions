# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxsum = float('-inf')
        
        def helper(node):
            nonlocal maxsum
            if not node:
                return 0
            #compute left max and right max without split (i.e. left + right + root)
            leftmax = helper(node.left)
            rightmax = helper(node.right)
            leftmax = max(leftmax,0) #skip -ve values
            rightmax = max(rightmax,0)
            maxsum = max(maxsum,leftmax+rightmax+node.val)
            #return maxpath sum with split (i.e. max(root+left,root+right)    
            return node.val + max(leftmax,rightmax)
        helper(root)
        return maxsum