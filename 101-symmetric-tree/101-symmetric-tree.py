# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return Ture 
        stack = [(root.left, root.right)]
        while stack:
            a,b = stack.pop(0)
            if a and b and a.val == b.val:
                stack.append((a.left, b.right))
                stack.append((a.right, b.left))
            elif not (not a and not b):
                return False 
        return True 
                