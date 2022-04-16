# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []
        
        res = []
        temp = [(root, str(root.val))]
        
        while temp:
            node, tmp = temp.pop()
            if not node.left and not node.right:
                res.append(tmp) 
            if node.left:
                temp.append((node.left, tmp + "->" + str(node.left.val)))
                
            if node.right:
                temp.append((node.right, tmp + "->" + str(node.right.val)))
                
        return res 