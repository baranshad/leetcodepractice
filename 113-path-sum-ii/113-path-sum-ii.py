# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        
        ans = []
        stack = [(root, [root.val], root.val)]
        while stack:
            node, temp, sum1 = stack.pop()
            if sum1== targetSum and not node.left and not node.right:
                ans.append(temp)
                
            if node.left:
                stack.append((node.left, temp + [node.left.val], sum1+node.left.val))
                
            if node.right:
                stack.append((node.right, temp + [node.right.val], sum1+node.right.val))
                
        return ans 
    
