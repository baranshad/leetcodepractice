# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        ans = []
        def helper(root):
            if not root:
                return []
            else:
                helper(root.left)
                ans.append(root.val)
                helper(root.right)
                
        helper(root)
        return min([ans[i+1]-ans[i] for i in range(len(ans)-1)])