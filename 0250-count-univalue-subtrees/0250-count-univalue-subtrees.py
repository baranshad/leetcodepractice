# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        def helper(node):
            nonlocal count
            if node and not node.left and not node.right:
                count += 1 
                return True 
            
            is_uni = True 
            if node.left:
                is_uni = helper(node.left) and is_uni and node.left.val == node.val 
            if node.right:
                is_uni = helper(node.right) and is_uni and node.right.val == node.val 
                
            count += is_uni 
            return is_uni 
        
        count = 0 
        helper(root)
        return count