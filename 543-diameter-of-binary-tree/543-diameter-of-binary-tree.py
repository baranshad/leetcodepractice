# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def helper(root):
            nonlocal res 
            if not root:
                return 0 
            l = helper(root.left)
            r = helper(root.right)
            res = max(res, l+r)
            return 1 + max(l,r)
        
        res = 0
        helper(root)
        return res
        
        