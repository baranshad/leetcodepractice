# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        sl = []
        def inorder(root):
            if not root: return
            inorder(root.left)
            sl.append(root.val)
            inorder(root.right)
        inorder(root)
        return min(sl[i+1] - sl[i] for i in range(len(sl)-1))
                          
        