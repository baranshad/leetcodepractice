# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        def is_leaf(node):
            return node and not node.left and not node.right 
        
        stack = [root]
        total = 0 
        while stack:
            sub_root = stack.pop()
            if is_leaf(sub_root.left):
                total += sub_root.left.val 
            if sub_root.left:
                stack.append(sub_root.left)
            if sub_root.right:
                stack.append(sub_root.right)
            
                
        return total 
                