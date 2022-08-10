# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True 
        
        stack = [(root.left, root.right)]
        while stack:
            x,y = stack.pop()
            if x and y and x.val == y.val:
                stack.append((x.left, y.right))
                stack.append((x.right, y.left))
            elif not (not x and not y):
                return False 
        return True 
    
     