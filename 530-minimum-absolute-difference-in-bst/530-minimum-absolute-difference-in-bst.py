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
            helper(root.left)
            s1.append(root.val)
            helper(root.right)
            
        helper(root)
        return min(s1[i+1]-s1[i] for i in range(len(s1)-1))
        