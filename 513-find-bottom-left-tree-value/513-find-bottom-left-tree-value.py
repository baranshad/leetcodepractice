# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if not root:
            return None 
        
        q = deque()
        q.append(root)
        ans = []
        while q:
            size = len(q)
            temp = []
            for i in range(size):
                node = q.popleft()
                temp.append(node)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                    
            ans.append(temp)
        return ans[-1][0].val