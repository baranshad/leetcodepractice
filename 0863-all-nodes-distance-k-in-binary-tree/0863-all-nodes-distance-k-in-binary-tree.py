# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def dfs(root, par=None):
            if root:
                root.par = par
                dfs(root.left, root)
                dfs(root.right, root)
                
        dfs(root)
        
        q = deque([(target, 0)])
        seen = {target}
        
        while q:
            if q[0][1] == k:
                return [node.val for node, d in q]
            
            node, d = q.popleft()
            for nb in (node.left, node.right, node.par):
                if nb and nb not in seen:
                    seen.add(nb)
                    q.append((nb, d+1))
                    
        return []