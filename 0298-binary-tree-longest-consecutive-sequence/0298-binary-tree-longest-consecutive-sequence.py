# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        def helper(node, length):
            nonlocal ans 
            if node.left:
                if node.left.val == node.val + 1:
                    helper(node.left, length+1)
                else:
                    helper(node.left, 1)
                    
            if node.right:
                if node.right.val == node.val + 1:
                    helper(node.right, length+1)
                else:
                    helper(node.right, 1)
                    
            ans = max(ans, length)
            
        
        ans = 0 
        if root:
            helper(root, 1)
        return ans 