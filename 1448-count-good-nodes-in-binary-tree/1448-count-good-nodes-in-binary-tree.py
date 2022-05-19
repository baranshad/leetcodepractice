# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0 
        
        def helper(node, maxval):
            nonlocal count
            if not node:
                return 
            
            if node.val >= maxval:
                count +=1 
            
            if node.right:
                helper(node.right, max(node.val, maxval))
            
            if node.left:
                helper(node.left, max(node.val, maxval))
                
        helper(root, float(-inf))
        return count
                