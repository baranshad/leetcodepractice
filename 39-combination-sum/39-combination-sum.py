class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates and min(candidates) > target:
            return []
        
        ans = []
        def helper(path, idx):
            if sum(path) == target:
                ans.append(path[:])
                
            elif sum(path) < target:
                for i in range(idx, len(candidates)):
                    path.append(candidates[i])
                    helper(path, i)
                    path.pop()
                    
        helper([], 0)
        return ans 
    

    
