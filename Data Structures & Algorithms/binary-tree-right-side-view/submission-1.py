# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q = deque([root])
        res = [[root]]
        while q:
            qlen = len(q)
            levelItems = []
            print("qlen",qlen)
            for i in range(qlen):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                    levelItems.append(node.left)

                if node.right:
                    q.append(node.right)
                    levelItems.append(node.right)
                
                print("level items",levelItems)
            if(levelItems):
                res.append(levelItems)
        finalRes = []
        for item in res:
            rightElement = item.pop()
            finalRes.append(rightElement.val)
        return finalRes
            

