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
            return 
        
        def helper(root):
            if not root:
                return None ## return or return none or return [] are all correct 
            
            arr.append(root.val)
            for c in root.children:
                helper(c)
                
        arr = []
        helper(root)
        return arr