class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for i in nums:
            if i in d:
                d[i] +=1 
            else:
                d[i] = 1 
        temp = [j for j in d.values()]        
        return max(temp) >= 2 