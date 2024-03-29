# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        arr = []
        q = deque([root])
        while q:
            size  = len(q)
            temp = 0
            for i in range(size):
                node= q.popleft()
                temp += node.val 
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right) 
            arr.append(temp/size)    
        
        return arr
            