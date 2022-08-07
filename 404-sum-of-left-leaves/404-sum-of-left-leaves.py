# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        def isleaf(root):
            if root and not root.left and not root.right:
                return True 
            return False 
        
        count = 0
        res = [root]
        while res:
            root = res.pop()
            if isleaf(root.left):
                count += root.left.val
            if root.left:
                res.append(root.left)
            if root.right:
                res.append(root.right)
                
        return count 