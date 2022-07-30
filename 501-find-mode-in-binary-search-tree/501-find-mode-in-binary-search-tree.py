# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        res = 1 
        d = {}
        def check(node, d):
            if not node:
                return d 
            if node.val in d:
                d[node.val] += 1 
            else:
                d[node.val] = 1 
                
            if node.left:
                check(node.left, d)
            if node.right:
                check(node.right, d)
                
            return d 
        
        check(root, d)
        maxnum = max(d.values())
        return [i for i,j in d.items() if j == maxnum]