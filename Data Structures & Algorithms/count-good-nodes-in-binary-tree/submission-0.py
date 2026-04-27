# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        res = 0
        resArr = []
        def dfs(node,prevMax):
            nonlocal res, resArr
            if not node:
                return
            newMax = prevMax
            if node.val >= prevMax:
                res+=1
                resArr.append(node.val)
                newMax = node.val
            dfs(node.left,newMax)
            dfs(node.right,newMax)
        dfs(root,root.val)
        print("res arr",resArr)
        return res

        