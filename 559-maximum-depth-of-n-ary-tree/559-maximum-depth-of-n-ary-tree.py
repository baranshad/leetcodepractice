"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0 
        stack = []
        if root is not None:
            stack.append((1, root))
            
        depth = 0 
        while stack:
            curdepth, root = stack.pop()
            if root:
                depth = max(depth, curdepth)
                for c in root.children:
                    stack.append((curdepth +1, c))
                    
        return depth 