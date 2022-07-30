# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        d = set()
        arr = []
        def preorder(root):
            if not root:
                return 
            preorder(root.left)
            arr.append(root.val)
            preorder(root.right)
            return arr 
            
        preorder(root)
        for i in arr:
            n = k - i
            if n in d:
                return True 
            else:
                d.add(i)