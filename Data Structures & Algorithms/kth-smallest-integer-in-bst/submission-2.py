# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        inorderlist = []
        def inorder(node):
            nonlocal inorderlist
            if not node:
                return
          

            inorder(node.left)
            inorderlist.append(node.val)
            inorder(node.right)
        
        inorder(root)
        return inorderlist[k-1]