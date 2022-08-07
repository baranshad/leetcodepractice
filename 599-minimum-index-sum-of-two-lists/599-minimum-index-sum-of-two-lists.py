class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        d1 = {}
        d2 = {}
        
        for i, val in enumerate(list1):
            d1[val] = i 
            
        for j, val in enumerate(list2):
            if val in d1:
                d2[val] = d1[val] + j 
                
        return [i for i, j in d2.items() if j ==min(d2.values())]