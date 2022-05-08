# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        di = defaultdict(list)
        q = deque([(root, 0)])

        while q:
            node, col = q.popleft()
            if node:
                di[col].append(node.val)
                q.append((node.left, col-1))
                q.append((node.right, col+1))
                
        sorted_di = sorted(di.items(), key= lambda x:x[0])
        res = [i for j, i in sorted_di]
        return res 