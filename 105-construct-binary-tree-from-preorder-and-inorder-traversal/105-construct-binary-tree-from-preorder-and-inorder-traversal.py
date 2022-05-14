# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        valindex = {}
        for i, val in enumerate(inorder):
            valindex[val] = i 
            
        rootind = 0
        def helper(l,r):
            nonlocal rootind 
            if l > r :
                 return None 
                
            nodeval = preorder[rootind]
            root = TreeNode(nodeval)
            rootind += 1 
            root.left = helper(l, valindex[nodeval]-1)
            root.right = helper(valindex[nodeval]+1, r)
            return root 
        
        return helper(0, len(preorder)-1)
    
    
  
     
            