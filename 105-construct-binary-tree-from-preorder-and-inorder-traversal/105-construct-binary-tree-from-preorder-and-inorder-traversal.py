# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_index = {}
        for i, val in enumerate(inorder):
            inorder_index[val] = i 
        
        root_index = 0
        def helper(l,r):
            nonlocal root_index 
            
            if l > r:
                return None 
            
            rootval = preorder[root_index]
            root = TreeNode(rootval)
            
            root_index += 1 
            
            root.left = helper(l, inorder_index[rootval]-1 )
            root.right = helper(inorder_index[rootval] + 1, r)
            return root 
        
        return helper(0, len(preorder)-1)
    
    
  
     
            