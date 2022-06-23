class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        c_sorted = sorted(candidates)
        
        def helper(idx, temp, c_sorted):
            if sum(temp) == target:
                ans.append(temp[:])
                
            elif sum(temp) < target:
                for i in range(idx, len(c_sorted)):
                    if i> idx and c_sorted[i] == c_sorted[i-1]:
                        continue 
                    temp.append(c_sorted[i])
                    helper(i+1, temp, c_sorted)
                    temp.pop()
                    
        helper(0,[],c_sorted)
        return ans