class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def helper(path, idx):
            if len(path) == k:
                res.append(path[:])
                
            else:
                for i in range(1, n+1):
                    if i > idx:
                        path.append(i)
                        helper(path, i)
                        path.pop()
                        
        helper([], 0)
        return res 