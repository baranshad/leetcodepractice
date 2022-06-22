class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def helper(idx, temp):
            if sum(temp) == target:
                res.append(temp[:])
            
            elif sum(temp) < target:
                for i in range(idx,len(candidates)):
                    temp.append(candidates[i])
                    helper(i ,temp)
                    temp.pop()
                    
        helper(0, [])
        return res 
                    
                    
    
    
     
         
    

    
