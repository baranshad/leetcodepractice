# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(l, r):
            if l > r:
                return None 
            mid = l + (r-l)//2
            p = TreeNode(nums[mid])
            p.left = helper(l, mid-1)
            p.right = helper(mid+1, r)
            return p 
        
        return helper(0, len(nums)-1)