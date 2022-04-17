# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        ans = []
        def helper(root):
            if not root:
                return 0
            leftsum = helper(root.left)
            rightsum = helper(root.right)
            ans.append(leftsum + root.val + rightsum)
            return leftsum + root.val + rightsum
        
        helper(root)
        ans1 = collections.Counter(ans)
        t1= [i for i, j in ans1.items() if j == max(ans1.values())]
        return t1