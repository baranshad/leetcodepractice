# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def treesMatch(root1, root2):
            if (not root1) or (not root2):
                return (not root1) and (not root2)
            if root1.val != root2.val:
                return False

            leftMatch = treesMatch(root1.left, root2.left)
            rightMatch = treesMatch(root1.right, root2.right)
            return leftMatch and rightMatch
        

        if not root:
            return False
        
        if treesMatch(root, subRoot):
            return True
        
        leftMatch = self.isSubtree(root.left, subRoot)
        rightMatch = self.isSubtree(root.right, subRoot)
        return leftMatch or rightMatch
    
    
    
    
            