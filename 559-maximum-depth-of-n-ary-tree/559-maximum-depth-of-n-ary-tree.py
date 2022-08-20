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
        if root and not root.children:
            return 1 
        
        for c in root.children:
            depth = [self.maxDepth(c) for c in root.children]
            return max(depth) + 1 
            