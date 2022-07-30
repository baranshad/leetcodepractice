"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return root 
        
        def helper(root):
            for c in root.children:
                helper(c)
            res.append(root.val)
            return res 
        
        res = []
        helper(root)
        return res 