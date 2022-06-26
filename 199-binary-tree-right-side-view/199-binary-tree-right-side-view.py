# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
        def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
            if not root: return []
            res = []
            q = deque([root]) # q.append([root]) ## q.append(root.val) is wrong
            while q:
                size = len(q)
                for i in range(size):
                    temp = q.popleft()
                    if i == size -1:
                        res.append(temp.val)
                    if temp.left:
                        q.append(temp.left)
                    if temp.right:
                        q.append(temp.right)    
            return res 
                    