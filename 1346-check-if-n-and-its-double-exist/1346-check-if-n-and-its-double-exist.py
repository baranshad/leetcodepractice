class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        d = set()
        for i in arr:
            if i*2 in d or i/2 in d:
                return True 
            #if i not in d:
            d.add(i)
        return False 
    
     
     
       #arrDict ={}		
        #for num in arr:
            #if num * 2 in arrDict or num/2 in arrDict:
                #return True
            
            #if num not in arrDict:
                #arrDict[num] = None
        #return False