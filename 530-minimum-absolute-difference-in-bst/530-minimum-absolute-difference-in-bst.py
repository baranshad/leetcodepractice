# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        s1 = []
        def helper(root):
            if not root:
                return root 
            helper(root.right)
            s1.append(root.val)
            helper(root.left)
               
        helper(root)
        return min(s1[i]-s1[i+1] for i in range(len(s1)-1))
        