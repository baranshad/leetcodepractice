class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        prev = -inf     
        for idx, val in enumerate(nums):
            if val == 1:
                if idx - prev <= k:
                    return False
                else:
                    prev = idx
        return True
                
                
               
                
        #prev = -inf       
        #for idx, val in enumerate(nums):
            #if val == 1:
                #if idx - prev <= k:
                    #return False
                #else:
                    #prev = idx
        #return True