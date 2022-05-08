# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        pval = p.val 
        qval = q.val
        node = root
        while node:
            nodeval = node.val 
            if pval > nodeval and qval > nodeval:
                node = node.right 
            elif pval<nodeval and qval < nodeval:
                node = node.left 
            else:
                return node 