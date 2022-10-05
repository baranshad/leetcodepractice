"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        first, last = None, None 
        
        def helper(root):
            nonlocal first, last 
            if root: 
                helper(root.left)
                if last:
                    last.right = root 
                    root.left = last 
                else:
                    first = root 
                last = root 
                helper(root.right)
                
        if not root:
            return None 
        
        helper(root)
        last.right = first 
        first.left = last 
        return first 
                
            
   