"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return root 
        
        def preorder(root):
            if not root:
                return 
            arr.append(root.val)
            for c in root.children:
                preorder(c)
                
            return arr
        
    
        arr = []
        preorder(root)
        return arr
            