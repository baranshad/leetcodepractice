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
        
        elif not root.children:
            return 1 
        else:
            height = [self.maxDepth(c) for c in root.children]
            return max(height) +1 
                
        