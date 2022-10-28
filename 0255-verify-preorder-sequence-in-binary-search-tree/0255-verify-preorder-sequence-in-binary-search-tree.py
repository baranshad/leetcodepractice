class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        minmum = float('-inf')
        path = []
        for i in preorder:
            if i < minmum:
                return False 
            while path and i > path[-1]:
                minmum = path.pop()
            path.append(i)
        return True 
        
         