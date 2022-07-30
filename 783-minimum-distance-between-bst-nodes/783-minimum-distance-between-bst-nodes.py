# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        arr = []
        def inorder(root):
            if not root: return root 
            inorder(root.left)
            arr.append(root.val)
            inorder(root.right)
            return arr 
        
        inorder(root)
        res = min(arr[i+1]-arr[i] for i in range(len(arr)-1))
        return res 