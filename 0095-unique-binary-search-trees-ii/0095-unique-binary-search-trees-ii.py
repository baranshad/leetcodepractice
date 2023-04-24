# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:

        if n <= 0:
            return []

        def helper(l, r):
            if l > r:
                return [None,]

            res = []
            for i in range(l, r+1):
                lt = helper(l,i-1)
                rt = helper(i+1, r)

                for j in lt:
                    for k in rt:
                        cur = TreeNode(i)
                        cur.left = j
                        cur.right = k 
                        res.append(cur)

            return res 

        return helper(1, n)
             