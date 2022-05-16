# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def preorder(root, q):
            if not root:
                return root
            q.append(root.val)
            preorder(root.left, q)
            preorder(root.right, q)
            
        q = []
        preorder(root, q)
        ans = 0
        for i in range(len(q)):
            if q[i] <= high and low <= q[i]:
                ans += q[i]
                
        return ans 