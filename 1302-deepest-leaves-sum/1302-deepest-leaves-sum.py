# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        def helper(node, depth):
            nonlocal maxd, res 
            if not node:
                return 
            if depth > maxd:
                maxd = depth
                res = 0 
            if depth == maxd:
                res += node.val 
                
            helper(node.left, depth+1)
            helper(node.right, depth+1)
            
        maxd = -1 
        res = 0 
        helper(root, 0)
        return res 