# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        arr = []
        def inorder(root):
            if not root: return root 
            inorder(root.left)
            arr.append(root.val)
            inorder(root.right)
            
            return arr 
        
        inorder(root)
        print(arr)
        arrset = [i for i in set(arr)]
        arrset = sorted(arrset)
        print(arrset)
        return arrset[1] if len(arrset) > 1 else -1