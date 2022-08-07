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
        stack.append((1,root))
        depth = 0
        while stack:
            currentdepth, node = stack.pop()
            if node:
                depth = max(depth, currentdepth)
                for c in node.children:
                    stack.append((currentdepth+1, c))
                    
        return depth 
                
        