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
        
        #stack = [root]
        res = []
        def preorder(node):
            res.append(node.val)
            for c in node.children:
                if c:
                    preorder(c)
                    
        preorder(root)
        return res 
            