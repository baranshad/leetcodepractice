# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return None 
        stack = [(root, str(root.val))]
        res = []
        while stack:
            node, path = stack.pop()
            if not node.left and not node.right:
                res.append(path)
            
            if node.left:
                stack.append((node.left, path+str(node.left.val)))
                
            if node.right:
                stack.append((node.right, path + str(node.right.val)))
         
        allval = 0
        for c in res:
            allval += int(c)
        return allval
                
                
        