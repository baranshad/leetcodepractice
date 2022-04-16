# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0 
        
        if not root.left and not root.right:
            return 1
        
        mind = float('inf')
        if root.left:
            mind = min(self.minDepth(root.left), mind)
        if root.right:
            mind = min(self.minDepth(root.right), mind)
            
        return mind+1