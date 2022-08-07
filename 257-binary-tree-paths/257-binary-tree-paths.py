# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def helper(root, res):
            if not root:
                return ""
            else:
                res += str(root.val)
                if not root.left and not root.right:
                    arr.append(res)
                else:
                    res += '->'
                    helper(root.left, res)
                    helper(root.right, res)
                
        
        arr = []
        helper(root, "")
        return arr 