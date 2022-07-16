# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        
        else:
            res=  str(root.val)
            left = self.tree2str(root.left)
            right = self.tree2str(root.right)
            
            leftstr =  "(" + str(left) + ")" if left or right else ""
            rightstr = "(" + str(right) + ")" if right else ""
            return res + leftstr + rightstr
            
            
 