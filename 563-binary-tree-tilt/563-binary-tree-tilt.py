# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        res = 0
        def helper(root):
            nonlocal res 
            if not root:
                return 0 
            l = helper(root.left)
            r = helper(root.right)
            till = abs(l-r)
            res += till 
            return root.val + l + r 
        helper(root)
        return res 
        
            
        