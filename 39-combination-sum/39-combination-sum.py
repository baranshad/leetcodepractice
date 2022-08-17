class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def helper(temp, idx):
            if sum(temp) == target:
                ans.append(temp[:])
                return 
                
            elif sum(temp) < target:
                for i in range(idx, len(candidates)):
                    temp.append(candidates[i])
                    helper(temp, i)
                    temp.pop()
                    
        helper([], 0)
        return ans 